import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

# Datos de ejemplo
videos = [
    {"id": 1, "contenido": "Video 1", "interacciones": 1000, "imagen": "1.png"},
    {"id": 2, "contenido": "Video 2", "interacciones": 500, "imagen": "2.png"},
    {"id": 3, "contenido": "Video 3", "interacciones": 2000, "imagen": "3.png"},
    {"id": 4, "contenido": "Video 4", "interacciones": 800, "imagen": "4.png"},
    {"id": 5, "contenido": "Video 5", "interacciones": 1500, "imagen": "5.png"}
]

# Crear grafo no dirigido
grafo = nx.Graph()

# Agregar nodos al grafo
for i, video in enumerate(videos):
    usuario = f"Usuario {i + 1}"
    grafo.add_node(video["id"], usuario=usuario, interacciones=video["interacciones"], imagen=video["imagen"])

# Agregar aristas al grafo
for i in range(len(videos)):
    for j in range(i + 1, len(videos)):
        interacciones = abs(videos[i]["interacciones"] - videos[j]["interacciones"])
        grafo.add_edge(videos[i]["id"], videos[j]["id"], interacciones=interacciones)

# Variables globales
index_actual = 0
videos_ordenados = []

# Función para mostrar las recomendaciones
def mostrar_recomendaciones():
    global index_actual, videos_ordenados
    recomendaciones = nx.pagerank(grafo, alpha=0.85)
    videos_ordenados = sorted(recomendaciones, key=recomendaciones.get, reverse=True)
    if not videos_ordenados:
        messagebox.showinfo("Recomendaciones", "No hay videos disponibles.")
        return
    index_actual = 0
    cargar_y_mostrar_imagen(videos_ordenados[index_actual])

# Función para cargar y mostrar imágenes
def cargar_y_mostrar_imagen(video_id):
    global index_actual
    video = grafo.nodes[video_id]
    imagen = Image.open(video["imagen"])
    imagen = imagen.resize((300, 300), Image.ANTIALIAS)
    imagen_tk = ImageTk.PhotoImage(imagen)
    panel.configure(image=imagen_tk)
    panel.image = imagen_tk
    ventana.title(f"TikTok - {video['usuario']}")

# Función para mostrar la imagen anterior
def mostrar_anterior():
    global index_actual
    if index_actual > 0:
        index_actual -= 1
        cargar_y_mostrar_imagen(videos_ordenados[index_actual])

# Función para mostrar la siguiente imagen
def mostrar_siguiente():
    global index_actual
    if index_actual < len(videos_ordenados) - 1:
        index_actual += 1
        cargar_y_mostrar_imagen(videos_ordenados[index_actual])

# Función para visualizar el grafo
def visualizar_grafo():
    pos = nx.spring_layout(grafo)
    plt.figure(figsize=(8, 6))
    node_labels = {node: data["usuario"] for node, data in grafo.nodes(data=True)}
    edge_labels = {(u, v): data["interacciones"] for u, v, data in grafo.edges(data=True)}
    nx.draw_networkx(grafo, pos, with_labels=True, labels=node_labels, node_size=500, node_color='skyblue',
                     font_size=10, font_color='black', edge_color='gray')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Grafo de Recomendaciones")
    plt.axis('off')
    plt.show()

# Crear ventana
ventana = tk.Tk()
ventana.title("TikTok - Recomendaciones")
ventana.geometry("600x500")

# Panel de la imagen
panel = tk.Label(ventana)
panel.pack(pady=10)

# Botones
btn_recomendaciones = tk.Button(ventana, text="Mostrar Recomendaciones", command=mostrar_recomendaciones)
btn_recomendaciones.pack(pady=10)

btn_anterior = tk.Button(ventana, text="Anterior", command=mostrar_anterior)
btn_anterior.pack(side=tk.LEFT)

btn_siguiente = tk.Button(ventana, text="Siguiente", command=mostrar_siguiente)
btn_siguiente.pack(side=tk.LEFT)

btn_visualizar_grafo = tk.Button(ventana, text="Visualizar Grafo", command=visualizar_grafo)
btn_visualizar_grafo.pack(pady=10)

ventana.mainloop()
