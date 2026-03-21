import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Configuración de página ---
st.set_page_config(
    page_title="Dashboard de Ventas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

COLORS = ["#00d4aa", "#ff6b6b", "#4ecdc4", "#45b7d1", "#96ceb4", "#feca57"]
PLOTLY_TEMPLATE = "plotly_dark"


@st.cache_data
def cargar_datos():
    df = pd.read_excel("data/supermarket_sales.xlsx")
    df["Date"] = pd.to_datetime(df["Date"])
    return df


df = cargar_datos()

# ============================================================
# SIDEBAR — Filtros
# ============================================================
st.sidebar.header("Filtros")

fecha_min, fecha_max = df["Date"].min().date(), df["Date"].max().date()
rango_fechas = st.sidebar.date_input(
    "Rango de fechas",
    value=(fecha_min, fecha_max),
    min_value=fecha_min,
    max_value=fecha_max,
)

ciudades = st.sidebar.multiselect(
    "Ciudad",
    options=df["City"].unique(),
    default=df["City"].unique(),
)

productos = st.sidebar.multiselect(
    "Línea de producto",
    options=df["Product line"].unique(),
    default=df["Product line"].unique(),
)

tipo_cliente = st.sidebar.radio(
    "Tipo de cliente",
    options=["Todos", "Member", "Normal"],
)

genero = st.sidebar.radio(
    "Género",
    options=["Todos", "Male", "Female"],
)

# --- Aplicar filtros ---
mask = (
    (df["Date"].dt.date >= rango_fechas[0])
    & (df["Date"].dt.date <= rango_fechas[1])
    & (df["City"].isin(ciudades))
    & (df["Product line"].isin(productos))
)
if tipo_cliente != "Todos":
    mask &= df["Customer type"] == tipo_cliente
if genero != "Todos":
    mask &= df["Gender"] == genero

df_filtrado = df[mask]

# ============================================================
# HEADER — KPIs
# ============================================================
st.markdown("# 📊 Dashboard de Ventas")
st.markdown("---")

if df_filtrado.empty:
    st.warning("No hay datos para los filtros seleccionados.")
    st.stop()

ventas_totales = df_filtrado["Total"].sum()
ingreso_bruto = df_filtrado["gross income"].sum()
rating_prom = df_filtrado["Rating"].mean()
transacciones = len(df_filtrado)

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Ventas Totales", f"${ventas_totales:,.2f}")
col2.metric("📈 Ingreso Bruto", f"${ingreso_bruto:,.2f}")
col3.metric("⭐ Rating Promedio", f"{rating_prom:.2f}")
col4.metric("🧾 Transacciones", f"{transacciones:,}")

st.markdown("---")

# ============================================================
# FILA 1 — Ventas por Ciudad / Línea de Producto
# ============================================================
col_izq, col_der = st.columns(2)

with col_izq:
    ventas_ciudad = (
        df_filtrado.groupby("City")["Total"]
        .sum()
        .sort_values()
        .reset_index()
    )
    fig_ciudad = px.bar(
        ventas_ciudad,
        x="Total",
        y="City",
        orientation="h",
        title="Ventas por Ciudad",
        color="City",
        color_discrete_sequence=COLORS,
        template=PLOTLY_TEMPLATE,
    )
    fig_ciudad.update_layout(showlegend=False, yaxis_title="", xaxis_title="Total ($)")
    st.plotly_chart(fig_ciudad, width="stretch")

with col_der:
    ventas_producto = (
        df_filtrado.groupby("Product line")["Total"]
        .sum()
        .sort_values()
        .reset_index()
    )
    fig_producto = px.bar(
        ventas_producto,
        x="Total",
        y="Product line",
        orientation="h",
        title="Ventas por Línea de Producto",
        color="Product line",
        color_discrete_sequence=COLORS,
        template=PLOTLY_TEMPLATE,
    )
    fig_producto.update_layout(showlegend=False, yaxis_title="", xaxis_title="Total ($)")
    st.plotly_chart(fig_producto, width="stretch")

# ============================================================
# FILA 2 — Distribuciones (Donut charts)
# ============================================================
col_izq2, col_der2 = st.columns(2)

with col_izq2:
    pago_dist = df_filtrado["Payment"].value_counts().reset_index()
    pago_dist.columns = ["Payment", "count"]
    fig_pago = px.pie(
        pago_dist,
        values="count",
        names="Payment",
        title="Métodos de Pago",
        hole=0.45,
        color_discrete_sequence=COLORS,
        template=PLOTLY_TEMPLATE,
    )
    fig_pago.update_traces(textinfo="percent+label")
    st.plotly_chart(fig_pago, width="stretch")

with col_der2:
    genero_dist = df_filtrado["Gender"].value_counts().reset_index()
    genero_dist.columns = ["Gender", "count"]
    fig_genero = px.pie(
        genero_dist,
        values="count",
        names="Gender",
        title="Ventas por Género",
        hole=0.45,
        color_discrete_sequence=["#00d4aa", "#ff6b6b"],
        template=PLOTLY_TEMPLATE,
    )
    fig_genero.update_traces(textinfo="percent+label")
    st.plotly_chart(fig_genero, width="stretch")

# ============================================================
# FILA 3 — Tendencia temporal
# ============================================================
ventas_diarias = (
    df_filtrado.groupby(df_filtrado["Date"].dt.date)["Total"]
    .sum()
    .reset_index()
)
ventas_diarias.columns = ["Fecha", "Total"]

fig_temporal = px.area(
    ventas_diarias,
    x="Fecha",
    y="Total",
    title="Tendencia de Ventas Diarias",
    template=PLOTLY_TEMPLATE,
    color_discrete_sequence=["#00d4aa"],
)
fig_temporal.update_layout(xaxis_title="", yaxis_title="Total ($)")
st.plotly_chart(fig_temporal, width="stretch")

# ============================================================
# FILA 4 — Rating por producto / Top transacciones
# ============================================================
col_izq3, col_der3 = st.columns(2)

with col_izq3:
    rating_producto = (
        df_filtrado.groupby("Product line")["Rating"]
        .mean()
        .sort_values()
        .reset_index()
    )
    fig_rating = px.bar(
        rating_producto,
        x="Rating",
        y="Product line",
        orientation="h",
        title="Rating Promedio por Producto",
        color="Rating",
        color_continuous_scale=["#ff6b6b", "#feca57", "#00d4aa"],
        template=PLOTLY_TEMPLATE,
    )
    fig_rating.update_layout(yaxis_title="", xaxis_title="Rating")
    st.plotly_chart(fig_rating, width="stretch")

with col_der3:
    st.markdown("#### 🏆 Top 10 Transacciones")
    top_ventas = (
        df_filtrado.nlargest(10, "Total")[
            ["Date", "City", "Product line", "Total", "Rating"]
        ]
        .reset_index(drop=True)
    )
    top_ventas.index += 1
    top_ventas["Total"] = top_ventas["Total"].apply(lambda x: f"${x:,.2f}")
    top_ventas["Date"] = top_ventas["Date"].dt.strftime("%Y-%m-%d")
    top_ventas.columns = ["Fecha", "Ciudad", "Producto", "Total", "Rating"]
    st.dataframe(top_ventas, width="stretch", height=390)
