import customtkinter
from CTkTable import CTkTable
from configs import Configs
from PIL import Image


def create_class_view(self, master, class_name, configs: Configs):
    """Função para criar uma tela padronizada do app, com base na classe esperada"""

    """-------------------CABEÇALHO-------------------"""
    self.title_frame = customtkinter.CTkFrame(master=master, fg_color="transparent")
    self.title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

    self.title_label = customtkinter.CTkLabel(
        master=self.title_frame,
        text=class_name,
        font=("Arial Black", 25),
        text_color="#004492",
    ).pack(anchor="nw", side="left")

    self.plus_button = customtkinter.CTkButton(
        master=self.title_frame,
        text="+ Adicionar",
        font=("Arial Black", 15),
        text_color="#fff",
        fg_color="#004492",
        hover_color="#3d81ca",
    ).pack(anchor="ne", side="right")

    """-------------------MÉTRICAS-------------------"""

    self.metrics_frame = customtkinter.CTkFrame(master=master, fg_color="transparent")
    self.metrics_frame.pack(anchor="n", fill="x", padx=27, pady=(36, 0))

    self.total_metric = customtkinter.CTkFrame(
        master=self.metrics_frame, fg_color="#004492", width=200, height=60
    )
    self.total_metric.grid_propagate(0)
    self.total_metric.pack(side="left")

    motorista_image_data = Image.open("./assets/motorista.png")
    motorista_img = customtkinter.CTkImage(
        light_image=motorista_image_data, dark_image=motorista_image_data, size=(43, 43)
    )
    self.motorista_image = customtkinter.CTkLabel(
        master=self.total_metric, image=motorista_img, text=""
    ).grid(row=0, column=0, rowspan=2, padx=(12, 5), pady=10)

    self.motorista_image_label = customtkinter.CTkLabel(
        master=self.total_metric,
        text="Total",
        text_color="#fff",
        font=("Arial Black", 15),
    ).grid(row=0, column=1, sticky="sw")

    self.motorista_total = customtkinter.CTkLabel(
        master=self.total_metric,
        text="123",
        text_color="#fff",
        font=("Arial Black", 15),
        justify="left",
    ).grid(row=1, column=1, sticky="nw", pady=(0, 10))

    """-------------------TABELA-------------------"""

    table_data = [
        ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"],
        ["3833", "Smartphone", "Alice", "123 Main St", "Confirmed", "8"],
        ["6432", "Laptop", "Bob", "456 Elm St", "Packing", "5"],
        ["2180", "Tablet", "Crystal", "789 Oak St", "Delivered", "1"],
        ["5438", "Headphones", "John", "101 Pine St", "Confirmed", "9"],
        ["9144", "Camera", "David", "202 Cedar St", "Processing", "2"],
        ["7689", "Printer", "Alice", "303 Maple St", "Cancelled", "2"],
        ["1323", "Smartwatch", "Crystal", "404 Birch St", "Shipping", "6"],
        ["7391", "Keyboard", "John", "505 Redwood St", "Cancelled", "10"],
        ["4915", "Monitor", "Alice", "606 Fir St", "Shipping", "6"],
        ["5548", "External Hard Drive", "David", "707 Oak St", "Delivered", "10"],
        ["5485", "Table Lamp", "Crystal", "808 Pine St", "Confirmed", "4"],
        ["7764", "Desk Chair", "Bob", "909 Cedar St", "Processing", "9"],
        ["8252", "Coffee Maker", "John", "1010 Elm St", "Confirmed", "6"],
        ["2377", "Blender", "David", "1111 Redwood St", "Shipping", "2"],
        ["5287", "Toaster", "Alice", "1212 Maple St", "Processing", "1"],
        ["7739", "Microwave", "Crystal", "1313 Cedar St", "Confirmed", "8"],
        ["3129", "Refrigerator", "John", "1414 Oak St", "Processing", "5"],
        ["4789", "Vacuum Cleaner", "Bob", "1515 Pine St", "Cancelled", "10"],
    ]

    self.table_frame = customtkinter.CTkScrollableFrame(
        master=master, fg_color="transparent"
    )
    self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)

    self.table = CTkTable(
        master=self.table_frame,
        values=table_data,
        text_color="#000",
        colors=["#E6E6E6", "#a3b0c3"],
        header_color="#004492",
        hover_color="#B4B4B4",
    )
    self.table.edit_row(0, text_color="#fff", hover_color="#004492")
    self.table.pack(expand=True)
