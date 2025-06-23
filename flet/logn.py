import flet as f 
def main(page: f.Page):
    page.bgcolor= "blue"
    page.title = "CupertinoLisr"
    def cambio(e):
        print("le diste click")
    cupertino = f.CupertinoListTile(
        title= f.Row([f.Text("ESTE CONTRO ES TREMENDAMENTE PRO", size=30), f.Text("CAn")]),
        subtitle= f.Text("Subtitlo del control"),
        leading= f.Icon(f.Icons.ADD_ALERT),
        trailing= f.Icon(f.Icons.MEDIA_BLUETOOTH_OFF),
        bgcolor= "white",
        additional_info= f.Text("CANCILLATE"),
        on_click=cambio,
        bgcolor_activated="red",
        url="www.google.com"
    )
    page.add(cupertino)
f.app(target=main)