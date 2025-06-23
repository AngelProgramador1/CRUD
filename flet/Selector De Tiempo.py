import flet as f 
def main(page: f.Page):
    page.title = "Selector de Tiempo de Angel"
    page.bgcolor= "cyan"

    def handle_change(e):
        page.add(f.Text(f"Tu hora es {TimerPiker.value}"))
    
    

    TimerPiker = f.TimePicker(
    confirm_text="SEGURO",
    cancel_text="No SEGURO",
    help_text="Elige tu hora",
    error_invalid_text="HORA MALA",
    hour_label_text="HORA",
    minute_label_text="MINUTO",
    on_change= handle_change
    )
    
    boton = f.ElevatedButton("Yo no tengo", on_click=lambda e: page.open(TimerPiker))
    page.add(boton)
f.app(target=main)