from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.services import LogisticaService

app = FastAPI(title="Dashboard Inteligencia Operativa")

# Configuración de templates y archivos estáticos
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

service = LogisticaService()


@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    """Renderiza el dashboard completo en la carga inicial (SSR completo)."""
    kpis = service.get_kpis()
    stock_critico = service.get_stock_critico(region="Todas")
    volume_data = service.get_volume_data(filtro="hoy")

    # Pasamos el request como parámetro directo de la función para complacer al framework
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "kpis": kpis,
            "stock_critico": stock_critico,
            "volume_data": volume_data
        }
    )


@app.get("/component/stock", response_class=HTMLResponse)
async def get_stock_partial(request: Request, region: str = Query("Todas")):
    """Endpoint Parcial: HTMX llama aquí para actualizar solo la tabla de stock."""
    stock_critico = service.get_stock_critico(region=region)

    return templates.TemplateResponse(
        request=request,
        name="partials/table_stock.html",
        context={"stock_critico": stock_critico}
    )


@app.get("/component/volume", response_class=HTMLResponse)
async def get_volume_partial(request: Request, filtro: str = Query("hoy")):
    """Endpoint Parcial: HTMX llama aquí para actualizar el componente de volumen."""
    volume_data = service.get_volume_data(filtro=filtro)

    return templates.TemplateResponse(
        request=request,
        name="partials/chart_volume.html",
        context={"volume_data": volume_data}
    )