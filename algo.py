import tkinter as tk
from tkinter import ttk
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

optimization_done = False #Flag to check if optimization has been done
optimized_path = [] #List of nodes in the optimized path

def load_data_from_txt(file_path): #Load data from txt file
    dataframe = pd.read_csv(file_path, sep='\t', header=None,
                            names=['Clock Speed', 'Voltage', 'Wattage', 'FPS', 'FPS/Watt'])
    return dataframe

def greedy_best_first_search(dataframe, start_index=0, logging=False):
    open_list = [start_index] #Intializing open and closed lists
    closed_list = set()
    best_node = {'index': start_index, 'value': dataframe.iloc[start_index]['FPS/Watt']} #Using the first node as the default best node
    path_taken = []

    # Initialize the graph
    G = nx.DiGraph()

    for i in range(len(dataframe)): #Adding nodes and edges to the graph
        G.add_node(i, label=f'Node {i}\nFPS/Watt: {dataframe.iloc[i]["FPS/Watt"]}')
        if i < len(dataframe) - 1:
            G.add_edge(i, i + 1)
        if i < len(dataframe) - 2:
            G.add_edge(i, i + 2)

    while open_list: 
        current_index = open_list.pop(0) #Taking the first node in the open list as the current node, removing it from the open list and adding it to the closed list
        current_node = dataframe.iloc[current_index]
        closed_list.add(current_index)

        if logging: #Logging the current node
            log_message(f"Exploring node {current_index} with FPS/Watt: {current_node['FPS/Watt']}")

        if path_taken: #Adding the edge to the graph
            G.add_edge(path_taken[-1], current_index, color='red', width=2)

        path_taken.append(current_index)

        if current_node['FPS/Watt'] > best_node['value']: #Checking if the current node is better than the best node
            best_node = {'index': current_index, 'value': current_node['FPS/Watt']}
            if logging:
                log_message(f"New best node found: {best_node['index']} with FPS/Watt: {best_node['value']}")

        for i in range(1, 3): #Adding the next nodes to the open list
            next_index = current_index + i
            if next_index < len(dataframe) and next_index not in closed_list:
                open_list.append(next_index)

        open_list = sorted(set(open_list), key=lambda index: dataframe.iloc[index]['FPS/Watt'], reverse=True) #Sorting the open list by FPS/Watt

    return dataframe.iloc[best_node['index']], G, path_taken

def log_message(message): #Log message to the GUI
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)
    log_text.config(state=tk.DISABLED)

def optimize(): #Optimization function
    global optimization_done, optimized_path
    log_message("Starting Optimization...")
    file_path = 'gabo/dataset.txt'
    df_from_txt = load_data_from_txt(file_path)
    _, _, optimized_path = greedy_best_first_search(df_from_txt, logging=True)
    log_message("Optimization Complete.")
    optimization_done = True

def visualize_tree(): #Tree visualization function
    global optimization_done, optimized_path
    file_path = 'gabo/dataset.txt'
    df_from_txt = load_data_from_txt(file_path)
    _, G, _ = greedy_best_first_search(df_from_txt)

    tree_window = tk.Toplevel(root)
    tree_window.title("Search Tree Visualization")

    fig, ax = plt.subplots(figsize=(8, 6))

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, arrows=True, edge_color='grey')
    
    if optimization_done:
        path_edges = list(zip(optimized_path, optimized_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    canvas = FigureCanvasTkAgg(fig, master=tree_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Tkinter GUI setup
root = tk.Tk()
root.title("GABO")
root.geometry("700x480")
style = ttk.Style(root)
style.theme_use("default") 

l1 = tk.Label(root, text="GPU AI-Based Optimizer", font=('Times', 20))
l1.pack(side=tk.TOP)

top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X, pady=20)

button_size = 15

optimize_button = tk.Button(top_frame, text="Optimize", command=optimize, height=button_size, width=button_size,
                            bg="#FFEBD8", activebackground="#efd9c1")
optimize_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)

visualize_button = tk.Button(top_frame, text="Visualize Tree", command=visualize_tree, height=button_size, width=button_size,
                            bg="#FFEBD8", activebackground="#efd9c1")
visualize_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)

exit_button = tk.Button(top_frame, text="Exit", command=root.destroy, height=button_size, width=button_size,
                            bg="#FFEBD8", activebackground="#efd9c1")
exit_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)

bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

scrollbar = tk.Scrollbar(bottom_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

log_text = tk.Text(bottom_frame, height=20, state=tk.DISABLED, yscrollcommand=scrollbar.set)
log_text.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5)

scrollbar.config(command=log_text.yview)

root.mainloop()
