import tkinter as tk
import csv
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
import time
import webbrowser

from py2neo import Graph, Node, Relationship, walk, NodeMatcher, RelationshipMatcher, Subgraph
graph = Graph("bolt://localhost:7687", auth=("neo4j", "yooooooo"))


#data_info = [['Bulbasaur', 'Grass', '318'], ['Ivysaur', 'Grass', '405'], ['Venusaur', 'Grass', '525'], ['Charmander', 'Fire', '309'], ['Charmeleon', 'Fire', '405'], ['Charizard', 'Fire', '534'], ['Squirtle', 'Water', '314'], ['Wartortle', 'Water', '405'], ['Blastoise', 'Water', '530'], ['Caterpie', 'Bug', '195'], ['Metapod', 'Bug', '205'], ['Butterfree', 'Bug', '395'], ['Weedle', 'Bug', '195'], ['Kakuna', 'Bug', '205'], ['Beedrill', 'Bug', '395'], ['Pidgey', 'Normal', '251'], ['Pidgeotto', 'Normal', '349'], ['Pidgeot', 'Normal', '479'], ['Rattata', 'Normal', '253'], ['Raticate', 'Normal', '413'], ['Spearow', 'Normal', '262'], ['Fearow', 'Normal', '442'], ['Ekans', 'Poison', '288'], ['Arbok', 'Poison', '448'], ['Pikachu', 'Electric', '320'], ['Raichu', 'Electric', '485'], ['Sandshrew', 'Ground', '300'], ['Sandslash', 'Ground', '450'], ['Nidoran?', 'Poison', '275'], ['Nidorina', 'Poison', '365'], ['Nidoqueen', 'Poison', '505'], ['Nidoran?', 'Poison', '273'], ['Nidorino', 'Poison', '365'], ['Nidoking', 'Poison', '505'], ['Clefairy', 'Fairy', '323'], ['Clefable', 'Fairy', '483'], ['Vulpix', 'Fire', '299'], ['Ninetales', 'Fire', '505'], ['Jigglypuff', 'Normal', '270'], ['Wigglytuff', 'Normal', '435'], ['Zubat', 'Poison', '245'], ['Golbat', 'Poison', '455'], ['Oddish', 'Grass', '320'], ['Gloom', 'Grass', '395'], ['Vileplume', 'Grass', '490'], ['Paras', 'Bug', '285'], ['Parasect', 'Bug', '405'], ['Venonat', 'Bug', '305'], ['Venomoth', 'Bug', '450'], ['Diglett', 'Ground', '265'], ['Dugtrio', 'Ground', '425'], ['Meowth', 'Normal', '290'], ['Persian', 'Normal', '440'], ['Psyduck', 'Water', '320'], ['Golduck', 'Water', '500'], ['Mankey', 'Fighting', '305'], ['Primeape', 'Fighting', '455'], ['Growlithe', 'Fire', '350'], ['Arcanine', 'Fire', '555'], ['Poliwag', 'Water', '300'], ['Poliwhirl', 'Water', '385'], ['Poliwrath', 'Water', '510'], ['Abra', 'Psychic', '310'], ['Kadabra', 'Psychic', '400'], ['Alakazam', 'Psychic', '500'], ['Machop', 'Fighting', '305'], ['Machoke', 'Fighting', '405'], ['Machamp', 'Fighting', '505'], ['Bellsprout', 'Grass', '300'], ['Weepinbell', 'Grass', '390'], ['Victreebel', 'Grass', '490'], ['Tentacool', 'Water', '335'], ['Tentacruel', 'Water', '515'], ['Geodude', 'Rock', '300'], ['Graveler', 'Rock', '390'], ['Golem', 'Rock', '495'], ['Ponyta', 'Fire', '410'], ['Rapidash', 'Fire', '500'], ['Slowpoke', 'Water', '315'], ['Slowbro', 'Water', '490'], ['Magnemite', 'Electric', '325'], ['Magneton', 'Electric', '465'], ["Farfetch'd", 'Normal', '377'], ['Doduo', 'Normal', '310'], ['Dodrio', 'Normal', '470'], ['Seel', 'Water', '325'], ['Dewgong', 'Water', '475'], ['Grimer', 'Poison', '325'], ['Muk', 'Poison', '500'], ['Shellder', 'Water', '305'], ['Cloyster', 'Water', '525'], ['Gastly', 'Ghost', '310'], ['Haunter', 'Ghost', '405'], ['Gengar', 'Ghost', '500'], ['Onix', 'Rock', '385'], ['Drowzee', 'Psychic', '328'], ['Hypno', 'Psychic', '483'], ['Krabby', 'Water', '325'], ['Kingler', 'Water', '475'], ['Voltorb', 'Electric', '330'], ['Electrode', 'Electric', '490'], ['Exeggcute', 'Grass', '325'], ['Exeggutor', 'Grass', '530'], ['Cubone', 'Ground', '320'], ['Marowak', 'Ground', '425'], ['Hitmonlee', 'Fighting', '455'], ['Hitmonchan', 'Fighting', '455'], ['Lickitung', 'Normal', '385'], ['Koffing', 'Poison', '340'], ['Weezing', 'Poison', '490'], ['Rhyhorn', 'Ground', '345'], ['Rhydon', 'Ground', '485'], ['Chansey', 'Normal', '450'], ['Tangela', 'Grass', '435'], ['Kangaskhan', 'Normal', '490'], ['Horsea', 'Water', '295'], ['Seadra', 'Water', '440'], ['Goldeen', 'Water', '320'], ['Seaking', 'Water', '450'], ['Staryu', 'Water', '340'], ['Starmie', 'Water', '520'], ['Scyther', 'Bug', '500'], ['Jynx', 'Ice', '455'], ['Electabuzz', 'Electric', '490'], ['Magmar', 'Fire', '495'], ['Pinsir', 'Bug', '500'], ['Tauros', 'Normal', '490'], ['Magikarp', 'Water', '200'], ['Gyarados', 'Water', '540'], ['Lapras', 'Water', '535'], ['Ditto', 'Normal', '288'], ['Eevee', 'Normal', '325'], ['Vaporeon', 'Water', '525'], ['Jolteon', 'Electric', '525'], ['Flareon', 'Fire', '525'], ['Porygon', 'Normal', '395'], ['Omanyte', 'Rock', '355'], ['Omastar', 'Rock', '495'], ['Kabuto', 'Rock', '355'], ['Kabutops', 'Rock', '495'], ['Aerodactyl', 'Rock', '515'], ['Snorlax', 'Normal', '540'], ['Articuno', 'Ice', '580'], ['Zapdos', 'Electric', '580'], ['Moltres', 'Fire', '580'], ['Dratini', 'Dragon', '300'], ['Dragonair', 'Dragon', '420'], ['Dragonite', 'Dragon', '600'], ['Mewtwo', 'Psychic', '680'], ['Mew', 'Psychic', '600']]
deleted_data_info = []
data_info = []

frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#BEB2A7",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}
def init_trigger():
    clear_trigger()
    set_create_trigger()
    update_property = ['PageRank', 'Label_Propagation', 'Degree_Centrality', 'WCC']
    i = 0
    for property_name in update_property:
        set_update_trigger(i, property_name)
        i = i + 1
    set_delete_trigger()

def clear_trigger():
    cypher_query = """
        CALL apoc.trigger.removeAll()
        """
    graph.run(cypher_query)

def set_create_trigger():
    cypher_query = """
        CALL apoc.trigger.add(
            'createNodeTrigger', 
            'UNWIND $createdNodes as node
            WITH node
            WHERE NOT EXISTS(node.Cnt)
            SET node.deleted = False,
                node.time = toString(datetime()) + "(create)",
                node.Cnt =  1 
            ',{phase: 'before'}
        )
        """
    graph.run(cypher_query)

def set_update_trigger(num, property_name):
    cypher_query = f"""
        CALL apoc.trigger.add(
            'updataNodeTrigger_{num}', 
            'UNWIND apoc.trigger.propertiesByKey($assignedNodeProperties, "{property_name}") as prop
            WITH prop.node as node
            SET node.time = node.time + "," + toString(datetime()) + "({property_name} update)"
            SET node.Cnt = node.Cnt + 1
            ',{{}}
        )
        """
    graph.run(cypher_query)

def set_delete_trigger():
    cypher_query = """
        CALL apoc.trigger.add(
            'deletedNodeTrigger', 
            'UNWIND apoc.trigger.propertiesByKey($assignedNodeProperties, "deleted") as prop
            WITH prop.node as node
            SET node.time = node.time + "," + toString(datetime()) + "(deleted)"
            SET node.Cnt = node.Cnt + 1
            ',{}
        )
        """
    graph.run(cypher_query)

def treeview_sort_column(tv, col, reverse):

    def convert(value):
        try:
            if value.isnumeric():
                return int(value)
            else:
                return value
        except ValueError:
            return value

    selected_item = tv.focus()
    if selected_item:
        # 如果有選取的行，取消選取
        tv.selection_remove(selected_item)

    if col =="Cnt":
        l = [(convert(tv.set(k, col)), k) for k in tv.get_children('')]
    else:
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
    #i = cols.index(col)

    #l.sort(key=lambda t: t[i], reverse=reverse)
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col,command=lambda: treeview_sort_column(tv, col, not reverse))

def create_node_cypher(filename):
    file_path = f'data/{filename}'
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
    headerNum = len(header)

    # 初始化 Cypher 查詢字串
    cypher_query = f"""CALL apoc.periodic.iterate(
                \'LOAD CSV WITH HEADERS FROM "file:///{filename}" AS row RETURN row\',\n"""
    cypher_query += "'CREATE (n:Node {"
    # 遍歷每個列標題，並建立 Cypher 查詢字串
    for index, column in enumerate(header):
        # 取得列標題
        column_name = column.strip()
        # 將列標題新增至 Cypher 查詢字串，格式為 "column_name: row.column_name"
        cypher_query += f"{column_name}: row.{column_name}"
        # 如果不是最後一個列標題，新增逗號分隔符
        if index < headerNum - 1:
            cypher_query += ", "
    cypher_query += "})',{batchSize:1000, parallel:false})"
    # 回傳 Cypher 查詢字串和 header
    csvfile.close()
    # print(cypher_query)
    return cypher_query, header

def create_relation_cypher(filename, id_name):
    # Read the header from the CSV file
    file_path = f'data/{filename}'
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
    # Initialize Cypher query
    cypher_query = f"""CALL apoc.periodic.iterate(
                \'LOAD CSV WITH HEADERS FROM "file:///{filename}" AS row RETURN row\',\n"""
    # Create relationship Cypher query
    cypher_query += f"'MATCH (p1:Node {{{id_name}: row.{header[0]}}})\n"
    cypher_query += f"MATCH (p2:Node {{{id_name}: row.{header[1]}}})\n"
    cypher_query += f"CREATE (p1)-[:INTERACTS_WITH]->(p2)\n"
    cypher_query += "',{batchSize:1000, parallel:false})"
    csvfile.close()
    # print(cypher_query)
    return cypher_query

def create_cypher_json(filename):
    cypher_query = f"""CALL apoc.periodic.iterate(
                    'CALL apoc.load.json("file:///{filename}") YIELD value RETURN value',
                    'UNWIND value.vertices AS nodeData
                    CREATE (n:Node{{ _id: toString(nodeData._id) }}) SET n += nodeData',
                    {{ batchSize: 1000, parallel: false }}
                    )"""
    cypher_query2 = f"""CALL apoc.periodic.iterate(
                    'CALL apoc.load.json("file:///{filename}") YIELD value RETURN value',
                    'UNWIND value.edges AS edgeData
                    MATCH (source:Node {{ _id: edgeData._inV }}), (target:Node {{ _id: edgeData._outV }}) 
                    CREATE (source)-[:INTERACTS_WITH {{ label: edgeData._label }}]->(target)',
                    {{ batchSize: 1000, parallel: false }}
                    ) """
    graph.run(cypher_query)
    graph.run(cypher_query2)

def load_yeast_json():
    cypher_query = f"""CALL apoc.periodic.iterate(
                    'CALL apoc.load.json("file:///yeast.json") YIELD value RETURN value',
                    'UNWIND value.vertices AS nodeData
                    CREATE (n:Node{{ _id: toString(nodeData._id) }})
                      SET n.pin = toString(nodeData.pin),
                          n.short = toString(nodeData.short),
                          n.oid = toString(nodeData.oid),
                          n.long = toString(nodeData.long)',
                    {{ batchSize: 1000, parallel: false }}
                    )"""
    cypher_query2 = f"""CALL apoc.periodic.iterate(
                    'CALL apoc.load.json("file:///yeast.json") YIELD value RETURN value',
                    'UNWIND value.edges AS edgeData
                    MATCH (source:Node {{ _id: toString(edgeData._inV) }}), (target:Node {{ _id: toString(edgeData._outV) }}) 
                    CREATE (source)-[:INTERACTS_WITH {{ label: edgeData._label }}]->(target)',
                    {{ batchSize: 1000, parallel: false }}
                    ) """
    graph.run(cypher_query)
    graph.run(cypher_query2)

class WelcomePage(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#708090", height=431, width=626)
        main_frame.pack(fill="both", expand="true")

        self.geometry("626x431")
        self.resizable(0, 0)
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "blue"}

        label_welcome = tk.Label(main_frame, title_styles, text="Welcome to the App!")
        label_welcome.pack()

        button = tk.Button(main_frame, text="Start", command=self.show_app)
        button.pack()

    def show_app(self):
        tk.messagebox.showinfo("Information", "Welcome")
        root.deiconify()
        top.destroy()

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu1", menu=menu_file)
        menu_file.add_command(label="Home", command=lambda: parent.show_frame(Some_Widgets))
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application", command=lambda: parent.Quit_application())

        # menu_orders = tk.Menu(self, tearoff=0)
        # self.add_cascade(label="Menu2", menu=menu_orders)

        menu_pricing = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu2", menu=menu_pricing)
        menu_pricing.add_command(label="Deleted Nodes", command=lambda: parent.show_frame(PageOne))

        menu_operations = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu3", menu=menu_operations)
        menu_operations.add_command(label="Command Input", command=lambda: parent.show_frame(PageTwo))
        # menu_positions = tk.Menu(menu_operations, tearoff=0)
        # menu_operations.add_cascade(label="Menu5", menu=menu_positions)
        # menu_positions.add_command(label="Page Three", command=lambda: parent.show_frame(PageThree))
        # menu_positions.add_command(label="Page Four", command=lambda: parent.show_frame(PageFour))

        menu_help = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu4", menu=menu_help)
        menu_help.add_command(label="About", command=lambda: parent.OpenNewWindow())

        # menu_help = tk.Menu(self, tearoff=0)
        # self.add_cascade(label="Menu4", menu=menu_help)
        # menu_help.add_command(label="Open New Window", command=lambda: parent.OpenNewWindow())


class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        # self.resizable(0, 0) prevents the app from being resized
        self.geometry("1024x600")
        self.frames = {}
        pages = (Some_Widgets, PageOne, PageTwo, PageThree, PageFour)
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Some_Widgets)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def OpenNewWindow(self):
        OpenNewWindow()

    def Quit_application(self):
        self.destroy()


class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#BEB2A7", height=600, width=1024)
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        

class Some_Widgets(GUI):  # inherits from the GUI class
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)



        frame1 = tk.LabelFrame(self, frame_styles, text="Exist Data List")
        frame1.place(rely=0.2, relx=0.02, height=440, width=980)

        frame2 = tk.LabelFrame(self, frame_styles, text="Some Feature")
        frame2.place(rely=0.05, relx=0.02, height=60, width=980)

        # This is a treeview.
        tv1 = ttk.Treeview(frame1)
        tv1["show"] = "headings"  # removes empty column
        tv1.place(relheight=1, relwidth=0.995)
        treescroll = tk.Scrollbar(frame1)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")
        def tv1_click(event):
            item = tv1.selection()
            if item:

                sub_window = create_sub_window("詳細資訊",500,500)

                val = tv1.item(item, "value")
                if val and isinstance(val, tuple) and len(val) > 0:
                    self.result_text = scrolledtext.ScrolledText(sub_window, width=60, height=10)
                    self.result_text.pack(padx=10, pady=10, fill="both", expand=True, side="bottom")
                    # 在初始化部分加入tag設定
                    self.result_text.tag_configure("tag_center", justify='center')
                    self.result_text.tag_configure("tag_indent", lmargin1=20)
                    # 獲取TreeView的列標題
                    columns = tv1["columns"]
                    # 生成Cypher查詢的字符串
                    exclude_columns = ['deleted', 'Cnt', 'PageRank', 'Label_Propagation', 'Degree_Centrality', 'WCC', 'lifetime']
                    values_str = ', '.join([f'{column}: "{value}"' for column, value in zip(columns, val)\
                                              if column != 'isNew' and column not in exclude_columns])
                    # values_str = ', '.join([f'{column}: "{value}"' if isinstance(value, str) else f'{column}: {value}' \
                    #     for column, value in zip(columns, val) if column != 'isNew' and column not in exclude_columns])
                    # print(columns)
                    # print(val)
                    # print(values_str)

                    cypher_query = "MATCH (n:Node { " + values_str + " ,deleted:False}) RETURN n"
                    cypher_query2_1 = "MATCH (n:Node { " + values_str + " ,deleted:False})-[:INTERACTS_WITH]->(neighbor:Node{deleted:False})\
                                         RETURN count(neighbor)"
                    cypher_query2_2 = "MATCH (n:Node { " + values_str + " ,deleted:False})<-[:INTERACTS_WITH]-(neighbor:Node{deleted:False})\
                                         RETURN count(neighbor)"
                    cypher_query3_1 = "MATCH (n:Node { " + values_str + " ,deleted:False})-[:INTERACTS_WITH]->(neighbor:Node{deleted:False})\
                                         RETURN neighbor"
                    cypher_query3_2 = "MATCH (n:Node { " + values_str + " ,deleted:False})<-[:INTERACTS_WITH]-(neighbor:Node{deleted:False})\
                                         RETURN neighbor"
                    result = graph.run(cypher_query)
                    result2_1 = graph.evaluate(cypher_query2_1)
                    result2_2 = graph.evaluate(cypher_query2_2)
                    result3_1 = graph.run(cypher_query3_1)
                    result3_2 = graph.run(cypher_query3_2)
                    
                    # 顯示結果
                    for record in result:
                        node = record["n"]
                        properties = dict(node)
                        for key, value in properties.items():
                            if key != 'isNew' and key != 'time' and key != 'deleted':
                                self.result_text.insert(tk.END, f"{key}: {value}\n\n")
                        self.result_text.insert(tk.END, f"out degree: {result2_1}\n\n")
                        self.result_text.insert(tk.END, f"in degree: {result2_2}\n\n")
                        self.result_text.insert(tk.END, f"out neighbor:\n")
                        for node in result3_1:
                            node_data = node["neighbor"]
                            properties2 = dict(node_data)
                            new_data = {attr:properties2[attr] for attr in properties2 if not callable(properties2[attr])\
                                         and not attr.startswith("__") and not attr.startswith("isNew")\
                                         and not attr.startswith("time") and not attr.startswith("deleted")}
                            self.result_text.insert(tk.END, f"{new_data}\n")
                        self.result_text.insert(tk.END, f"\n")
                        self.result_text.insert(tk.END, f"in neighbor:\n")
                        for node in result3_2:
                            node_data = node["neighbor"]
                            properties2 = dict(node_data)
                            new_data = {attr:properties2[attr] for attr in properties2 if not callable(properties2[attr])\
                                         and not attr.startswith("__") and not attr.startswith("isNew")\
                                         and not attr.startswith("time") and not attr.startswith("deleted")}
                            self.result_text.insert(tk.END, f"{new_data}\n")
                        self.result_text.insert(tk.END, f"\n")
                        if 'time' in properties:
                            self.result_text.insert(tk.END, "time:\n")
                            timestamps = properties['time']
                            for timestamp in timestamps:
                                if timestamp == ',':
                                    self.result_text.insert(tk.END, f"\n")
                                else:
                                    self.result_text.insert(tk.END, f"{timestamp}")

                        # break
                else:
                    print("No value found in the selected item.")
            selected_item = tv1.focus()
            if selected_item:
                # 如果有選取的行，取消選取
                tv1.selection_remove(selected_item)

        button1 = tk.Button(frame2, text="Select dataset", command=lambda: show_dataset())
        button1.pack(side="left", padx=50, pady=10)
        def show_dataset():
            global sub_window_dataset
            ####
            if sub_window_dataset is not None and sub_window_dataset.winfo_exists():
                # 如果子視窗存在，則聚焦到子視窗
                sub_window_dataset.focus()

            else:
                # 創建子視窗
                sub_window_dataset = create_sub_window("選擇匯入的資料集",300,400)
                sub_window_dataset.resizable(0, 0)

                # 加入標籤
                label = tk.Label(sub_window_dataset, text="Please choose the dataset to load", padx=10, pady=10)
                label.pack()

                # 加入按鈕
                button1 = tk.Button(sub_window_dataset, text="Yesat(old)", command=lambda: load_old_yeast())
                button1.pack(side="top", pady=30)
                def load_old_yeast():
                    Clear_Exist_Database()
                    Clear_Deleted_Database()
                    filename = 'yeast_nodes.csv'
                    filename2 = 'yeast_relation.csv'
                    cypher_query, header = create_node_cypher(filename)
                    cypher_query2 = create_relation_cypher(filename2, header[0])
                    result = graph.run(cypher_query)
                    result = graph.run(cypher_query2)
                    Refresh_data()

                
                button2 = tk.Button(sub_window_dataset, text="Yesat(new)", command=lambda: load_new_yeast())
                button2.pack(side="top", pady=30)
                def load_new_yeast():
                    Clear_Exist_Database()
                    Clear_Deleted_Database()
                    load_yeast_json()
                    Refresh_data()
                
                button3 = tk.Button(sub_window_dataset, text="Mico", command=lambda: load_mico())
                button3.pack(side="top", pady=30)
                def load_mico(): #可能有問題
                    Clear_Exist_Database()
                    Clear_Deleted_Database()
                    create_cypher_json("mico.json")
                    Refresh_data()
                
                button4 = tk.Button(sub_window_dataset, text="Graph500", command=lambda: load_graph500())
                button4.pack(side="top", pady=30)
                def load_graph500():
                    filename = 'graph500_vertex.csv'
                    filename2 = 'graph500_edge.csv'
                    cypher_query, header = create_node_cypher(filename)
                    cypher_query2 = create_relation_cypher(filename2, header[0])
                    Clear_Exist_Database()
                    Clear_Deleted_Database()
                    result = graph.run(cypher_query)
                    result = graph.run(cypher_query2)
                    Refresh_data()

                sub_window_dataset.protocol("WM_DELETE_WINDOW", on_sub_window_dataset_close)
            
        def on_sub_window_dataset_close():
            global sub_window_dataset

            # 子視窗關閉時清空
            sub_window_dataset.destroy()
            sub_window_dataset = None
            

        def on_button_click(dataset_name):
            print(f"選擇的 dataset 是: {dataset_name}")


######## BenchMark Start ########

        button2 = tk.Button(frame2, text="Select Algorithm", command=lambda: show_algorithm())
        button2.pack(side="left", padx=50, pady=10)
        def show_algorithm():
            global sub_window_algorithm
            
            ####
            if sub_window_algorithm is not None and sub_window_algorithm.winfo_exists():
                # 如果子視窗存在，則聚焦到子視窗
                sub_window_algorithm.focus()

            else:

                # 創建子視窗
                sub_window_algorithm =  create_sub_window("選擇要使用的演算法",300,450)      
                sub_window_algorithm.resizable(0, 1)    

                # 創建核取方塊
                check_var = tk.IntVar(sub_window_algorithm)
                check_button = tk.Checkbutton(sub_window_algorithm, text="是否寫入結果至節點屬性", variable=check_var)
                check_button.pack(pady=10)

        #### Page Rank ####
                buttonPR = tk.Button(sub_window_algorithm, text="Page Rank", command=lambda: pagerank())
                buttonPR.pack(side="top", pady=20)

                def pagerank():
                    
                    create_graph()
                    
                    for _ in range(10):

                        if check_var.get():
                            cypher_query = "CALL gds.pageRank.write('test', {writeProperty:'PageRank', maxiterations:3, concurrency:4})"

                        else:
                            cypher_query = "CALL gds.pageRank.stream('test', {maxiterations:3, concurrency:4}) YIELD nodeId, score"
                        
                        #取得結果和時間
                        result, time_taken = algorithm_benchmark(cypher_query)  
                        print("執行時間:", time_taken, "s")

                    clear_graph()

                    # print("執行時間:", time_taken, "s")
                    # 結果顯示
                    # for record in result:
                    #     print(record)
                    Refresh_data()

        #### Label Propagation ####
                buttonLP = tk.Button(sub_window_algorithm, text="Label Propagation", command=lambda: labelpropagation())
                buttonLP.pack(side="top", pady=20)

                def labelpropagation():
                    
                    create_graph()

                    if check_var.get():
                        cypher_query = "CALL gds.labelPropagation.write('test', {writeProperty:'Label_Propagation', maxiterations:20, concurrency:4})"

                    else:
                        cypher_query = "CALL gds.labelPropagation.stream('test', {maxiterations:20, concurrency:4}) YIELD nodeId, communityId"
                    
                    #取得結果和時間
                    result, time_taken = algorithm_benchmark(cypher_query)
                    clear_graph()

                    print("執行時間:", time_taken, "s")
                    # 結果顯示
                    # for record in result:
                    #     print(record)
                    Refresh_data()

        #### Degree Centrality ####
                buttonDC = tk.Button(sub_window_algorithm, text="Degree Centrality", command=lambda: degreecentrality())
                buttonDC.pack(side="top", pady=20)

                def degreecentrality():

                    create_graph()

                    if check_var.get():
                        cypher_query = "CALL gds.degree.write('test', {writeProperty:'Degree_Centrality', relationshipWeightProperty:null, concurrency:4})"

                    else:
                        cypher_query = "CALL gds.degree.stream('test', {relationshipWeightProperty:null, concurrency:4}) YIELD nodeId, score"
                    
                    #取得結果和時間
                    result, time_taken = algorithm_benchmark(cypher_query)
                    clear_graph()

                    print("執行時間:", time_taken, "s")
                    # 結果顯示
                    # for record in result:
                    #     print(record)
                    Refresh_data()

        #### Weakly Connected Components  ####
                buttonWCC = tk.Button(sub_window_algorithm, text="Weakly Connected Components", command=lambda: wcc())
                buttonWCC.pack(side="top", pady=20)

                def wcc():

                    create_graph()

                    if check_var.get():
                        cypher_query = "CALL gds.wcc.write('test', {writeProperty:'WCC',concurrency:4})"

                    else:
                        cypher_query = "CALL gds.wcc.stream('test', {concurrency:4}) YIELD nodeId, componentId"
                    
                    #取得結果和時間
                    result, time_taken = algorithm_benchmark(cypher_query)
                    clear_graph()

                    print("執行時間:", time_taken, "s")
                    # 結果顯示
                    # for record in result:
                    #     print(record)
                    Refresh_data()

        #### Abstraction  ####
                buttonWCC = tk.Button(sub_window_algorithm, text="Abstraction(寫入)", command=lambda: abstraction())
                buttonWCC.pack(side="top", pady=20)

                def abstraction():

                    #### Case1 沒有出邊
                    cypher_query1_1 = "MATCH (n:Node{deleted:False}) WHERE NOT (n)-[]->() SET n.deleted = True"
                    cypher_query1_2 = "MATCH (n:Node{deleted:False})-[]->(outNeighbor:Node{deleted:True})\
                                       MATCH (n:Node{deleted:False})-[]->(inNeighbor)\
                                       WITH n, COUNT(outNeighbor) AS outCount, COUNT(inNeighbor) AS inCount WHERE outCount = inCount \
                                       SET n.deleted = True"

                    #### Case2 沒有入邊
                    cypher_query2_1 = "MATCH (n:Node{deleted:False}) WHERE NOT ()-[]->(n) SET n.deleted = True"
                    cypher_query2_2 = "MATCH (n:Node{deleted:False})<-[]-(inNeighbor:Node{deleted:True})\
                                       MATCH (n:Node{deleted:False})<-[]-(outNeighbor)\
                                       WITH n, COUNT(outNeighbor) AS outCount, COUNT(inNeighbor) AS inCount WHERE outCount = inCount \
                                       SET n.deleted = True"

                    #### Case3 只有一出邊一入邊
                    cypher_query3_1 = "MATCH (n:Node{deleted:False})-[]->(outNeighbor:Node{deleted:False}) \
                                       MATCH (n:Node{deleted:False})<-[]-(inNeighbor:Node{deleted:False}) WITH n, \
                                       COUNT(outNeighbor) AS outCount, \
                                       COUNT(inNeighbor) AS inCount \
                                       WHERE outCount = 1 AND inCount = 1\
                                       SET n.deleted = True\
                                       MERGE (inNeighbor)-[:INTERACTS_WITH]->(outNeighbor)"
                    # cypher_query3_2 = ""

                    start_time = time.time()  # 開始時間


                    
                    #### Case4 多個入邊
                    cypher_query4 = "MATCH (n:Node) RETURN COUNT(n)/100"
                    numA = graph.evaluate(cypher_query4)
                    # print(str(numA))

                    cypher_query4_1 = "\
                                    MATCH (start:Node{deleted:False})-[]->(n:Node{deleted:False}) WHERE not start = n \
                                    WITH n, COUNT(start) AS inDegree ORDER BY inDegree DESC limit "+str(numA)+"\
                                    WHERE inDegree > 10 RETURN n"
                    result = graph.evaluate(cypher_query4_1)
                    header_n = []
                    if result is None:
                        pass
                    else: ##### 取各個n點 #####
                        result = graph.run(cypher_query4_1)
                        for record in result:
                            node = record['n']  #這個n是看你return 什麼
                            # print("node")
                            properties = dict(node)
                            # print("prooerties")
                            # print(properties)
                            header_n= [attr for attr in properties if not callable(properties[attr])\
                                                            and not attr.startswith("__") ] 
                            # print("header")
                            # print(header)
                            value= [properties[attr] for attr in properties if not callable(properties[attr])\
                                                    and not attr.startswith("__") ]
                            # print("value")
                            # print(value)

                            exclude_columns = ['isNew', 'time', 'deleted', 'Cnt', 'PageRank', 'Label_Propagation', 'Degree_Centrality', 'WCC', 'lifetime']
                            values_str = ', '.join([f'{column}: "{value}"' for column, value in zip(header_n, value) \
                                                    if column not in exclude_columns])
                            
                            # print("values_str " + values_str)
                            
                            
                            ##### 看n是否deleted #####
                            cypher_query4_2 = "MATCH (n:Node{"+values_str+ "}) return n.deleted"
                            result2 = graph.evaluate(cypher_query4_2)
                            # print(type(result2))
                            if result2:
                                pass

                            else:
                                # print("no")
                                # print("MATCH (start:Node{deleted:False})-[]->(n:Node{"+values_str+ "})")
                                cypher_query4_3 = "MATCH (start:Node{deleted:False})-[]->(n:Node{"+values_str+ "}) WHERE not start = n \
                                                WITH  n, COUNT(start) AS inDegree\
                                                WHERE inDegree > 10\
                                                MATCH (start:Node{deleted:False})-[]->(n:Node{"+values_str+ "}) WHERE not start = n\
                                                RETURN start"
                                result3 = graph.evaluate(cypher_query4_3)
                                header_start = []
                                if result3 is None:
                                    # print("no")
                                    pass

                                else: ##### 取start各種屬性 #####
                                    result3 = graph.run(cypher_query4_3)
                                    # print(result3)
                                    for record in result3:
                                        node3 = record['start']
                                        # print("start node")
                                        # print(node)
                                        properties3 = dict(node3)
                                        # print("properties")
                                        # print(properties3)
                                        header_start= [attr for attr in properties3 if not callable(properties3[attr])\
                                                            and not attr.startswith("__") ] 
                                        # print("header")
                                        # print(header)
                                        value3= [properties3[attr] for attr in properties3 if not callable(properties3[attr])\
                                                                and not attr.startswith("__") ]
                                        # print("value")
                                        # print(value)

                                        exclude_columns = ['isNew', 'time', 'deleted', 'Cnt', 'PageRank', 'Label_Propagation', 'Degree_Centrality', 'WCC', 'lifetime']
                                        values_str_start = ', '.join([f'{column}: "{value}"' for column, value in zip(header_start, value3) \
                                                                if column not in exclude_columns])
                                        # print("values_str_start " + values_str_start)


                                        ##### 找Start入邊 #####
                                        cypher_query4_4 = "MATCH (m:Node{deleted:False})-[]->(start:Node{"+values_str_start+ "})\
                                                        RETURN m"
                                        result4 = graph.evaluate(cypher_query4_4)
                                        header_in = []
                                        if result4 is None:
                                            pass
                                                                        
                                        else: ##### 取Start入邊的各種屬性 #####
                                            result4 = graph.run(cypher_query4_4)
                                            for record in result4:
                                                node4 = record['m']  #這個n是看你return 什麼
                                                properties4 = dict(node4)
                                                header_in= [attr for attr in properties4 if not callable(properties4[attr])\
                                                            and not attr.startswith("__") ] 
                                                # print("header")
                                                # print(header)
                                                value4= [properties4[attr] for attr in properties4 if not callable(properties4[attr])\
                                                                        and not attr.startswith("__") ]
                                                # print("value")
                                                # print(value)

                                                exclude_columns = ['isNew', 'time', 'deleted', 'Cnt', 'PageRank', 'Label_Propagation', 'Degree_Centrality', 'WCC', 'lifetime']
                                                values_str_m = ', '.join([f'{column}: "{value}"' for column, value in zip(header_in, value4) \
                                                                        if column not in exclude_columns])
                                                # print("values_str_m " + values_str_m)

                                                ## for 各個 start 入邊
                                                cypher_query4_5 = "MATCH (n:Node{" + values_str + "})\
                                                                MATCH (m:Node{" + values_str_m + "})\
                                                                MERGE (m)-[r:INTERACTS_WITH]->(n)"
                                                # print(cypher_query4_5)
                                                graph.run(cypher_query4_5)
                                        

                                        ##### 找Start出邊 #####
                                        cypher_query4_6 = "MATCH (m:Node{deleted:False})<-[]-(start:Node{"+values_str_start+ "})\
                                                        RETURN m"
                                        result6 = graph.evaluate(cypher_query4_6)
                                        header_out = []
                                        if result6 is None:
                                            pass
                                                                        
                                        else: ##### 取Start出邊的各種屬性 #####
                                            result6 = graph.run(cypher_query4_6)
                                            for record in result6:
                                                node6 = record['m']  #這個n是看你return 什麼
                                                properties6 = dict(node6)
                                                header_out= [attr for attr in properties6 if not callable(properties6[attr])\
                                                            and not attr.startswith("__") ] 
                                                # print("header")
                                                # print(header)
                                                value6= [properties6[attr] for attr in properties6 if not callable(properties6[attr])\
                                                                        and not attr.startswith("__") ]
                                                # print("value")
                                                # print(value)

                                                exclude_columns = ['isNew', 'time', 'deleted', 'Cnt', 'PageRank', 'Label_Propagation', 'Degree_Centrality', 'WCC', 'lifetime']
                                                values_str_m = ', '.join([f'{column}: "{value}"' for column, value in zip(header_out, value6) \
                                                                        if column not in exclude_columns])
                                                # print("values_str_m " + values_str_m)

                                                ## for 各個 start 出邊
                                                cypher_query4_7 = "MATCH (n:Node{" + values_str + "})\
                                                                MATCH (m:Node{" + values_str_m + "})\
                                                                MERGE (m)<-[r:INTERACTS_WITH]-(n)"
                                                # print(cypher_query4_7)
                                                graph.run(cypher_query4_7)



                                        ##### 修改n屬性 #####
                                        exclude_columns = ['isNew', 'time', 'deleted', 'Cnt', 'PageRank', 'Label_Propagation', 'Degree_Centrality', 'WCC', 'lifetime']
                                        values_str_start_properties = ', '.join([f'n.{column} = n.{column} +  ",{value}"' for column, value in zip(header_start, value3) \
                                                                if column not in exclude_columns])
                                        values_str_start_properties += ", n.Cnt = n.Cnt + 1 "

                                        # print("SET " + values_str_start_properties)

                                        cypher_query4_8 = "MATCH (n:Node{"+values_str+ "})\
                                                        SET " + values_str_start_properties 
                                        # print(cypher_query4_8)
                                        graph.run(cypher_query4_8)
                                        
                                        ##### 改start的deleted為true #####
                                        cypher_query4_9 = "MATCH (start:Node{"+values_str_start+ "})\
                                                        SET " + "start.deleted = True" 
                                        # print(cypher_query4_9)
                                        graph.run(cypher_query4_9)
                                        for key, value in properties.items():
                                            if key not in exclude_columns:
                                                properties[key] = value+"," +properties3[key]
                                        # print(properties)
                                        header_n= [attr for attr in properties if not callable(properties[attr])\
                                                                        and not attr.startswith("__") ] 
                                        value= [properties[attr] for attr in properties if not callable(properties[attr])\
                                                                and not attr.startswith("__") ]
                                        exclude_columns = ['isNew', 'time', 'deleted', 'Cnt', 'PageRank', 'Label_Propagation', 'Degree_Centrality', 'WCC', 'lifetime']
                                        values_str = ', '.join([f'{column}: "{value}"' for column, value in zip(header_n, value) \
                                                                if column not in exclude_columns])
                                #### 加入merge時間
                                cypher_query4_10 =  """MATCH (n:Node{""" +values_str +"""})
                                                       SET n.time = n.time + "," + toString(datetime()) + "(node merge)\" """
                                graph.run(cypher_query4_10)
                    
                    print("case 4 compelete")

                    graph.run(cypher_query1_1)
                    graph.run(cypher_query1_2)
                    print("case 1 compelete")
                    graph.run(cypher_query2_1)
                    graph.run(cypher_query2_2)
                    print("case 2 compelete")
                    graph.run(cypher_query3_1)
                    print("case 3 compelete")

                    end_time = time.time()    # 結束時間
                    time_taken = end_time - start_time

                    print("執行時間:", time_taken, "s")
                    # 結果顯示
                    # for record in result:
                    #     print(record)
                    Refresh_data()

        #### Others  ####
                buttonCLR = tk.Button(sub_window_algorithm, text="Clear(除錯用)", command=lambda: clear_graph())
                buttonCLR.pack(side="top", pady=20)

                buttonCTE = tk.Button(sub_window_algorithm, text="Create(除錯用)", command=lambda: create_graph())
                buttonCTE.pack(side="top", pady=20)

                buttonCTE = tk.Button(sub_window_algorithm, text="Delete Nodes(除錯用)", command=lambda: delete_all_data())
                buttonCTE.pack(side="top", pady=20)

                def create_graph():
                    cypher_query = "CALL gds.graph.create.cypher(\
                                    'test',\
                                    'MATCH (n:Node{deleted:false}) RETURN id(n) AS id, labels(n) AS labels',\
                                    'MATCH (n:Node{deleted:false})-[r:INTERACTS_WITH]->(m:Node{deleted:false}) \
                                    RETURN id(n) AS source, id(m) AS target, type(r) AS type, properties(r) AS properties'\
                                    )"
                    graph.run(cypher_query)
                    

                def clear_graph():
                    cypher_query = "CALL gds.graph.drop('test')"
                    graph.run(cypher_query)

                def delete_all_data():
                    cypher_query = "MATCH(n) DETACH DELETE n"
                    graph.run(cypher_query)
                    Refresh_data()
                    

                def algorithm_benchmark(query):
                    start_time = time.time()  # 開始時間
                    result = graph.run(query)
                    end_time = time.time()    # 結束時間
                    execution_time = end_time - start_time
                    return result, execution_time
                
            sub_window_algorithm.protocol("WM_DELETE_WINDOW", on_sub_window_algorithm_close)
            
        def on_sub_window_algorithm_close():
            global sub_window_algorithm

            # 子視窗關閉時清空
            sub_window_algorithm.destroy()
            sub_window_algorithm = None
        
######## BenchMark End ########


        button3 = tk.Button(frame2, text="Search", command=lambda: Search_Window())
        button3.pack(side="left", padx=50, pady=10)
        def Search_Window():
            global sub_window_search
            ####
            if sub_window_search is not None and sub_window_search.winfo_exists():
                # 如果子視窗存在，則聚焦到子視窗
                sub_window_search.focus()

            else:
                # 創建子視窗
                sub_window_search = create_sub_window("搜尋介面", 300, 350)
                sub_window_search.resizable(0, 1)

                # 加入標籤
                label = tk.Label(sub_window_search, text="Please choose the columns to search", padx=10, pady=10)
                label.pack()
                #frame_column = tk.LabelFrame(sub_window_search, frame_styles, text="columns name")
                #frame_column .place(rely=0.05, relx=0.45, height=50, width=50)

                # 加入搜索框
                search_entry = tk.Entry(sub_window_search)
                search_entry.pack()

                num_columns = len(tv1["columns"])
                
                # 單選的 IntVar
                var_column = tk.IntVar(sub_window_search)

                # 動態生成 Radiobutton
                radio_buttons = []
                selected_column = [0]
                def update_selected_column():
                    selected_column.clear()
                    selected_column.append(var_column.get())

                # 加入動態生成的 Radiobutton
                for i, column_id in enumerate(tv1["columns"]):
                    rb_col = tk.Radiobutton(sub_window_search, text=f"{column_id}", variable=var_column, value=i, command=update_selected_column)
                    rb_col.pack()
                    radio_buttons.append(rb_col)

                # 加入搜索按钮
                search_button = tk.Button(sub_window_search, text="Search", command=lambda: search_treeview(search_entry.get(), selected_column))
                search_button.pack()

                sub_window_search.protocol("WM_DELETE_WINDOW", on_sub_window_search_close)

        def on_sub_window_search_close():
            global sub_window_search

            # 子視窗關閉時清空
            sub_window_search.destroy()
            sub_window_search = None


        def search_treeview(search_term, selected_column):

            column_id = selected_column[0]
            # 遍歷所有數據行，只顯示符合條件的行
            for item_id in tv1.get_children():
                item = tv1.item(item_id)['values']
                if search_term.lower() in str(item[column_id]).lower():
                    pass
                else:
                    tv1.delete(item_id)

        values_num = [2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]

        spinbox = tk.Spinbox(frame2, values=values_num, width=6, state="normal")
        spinbox.pack(side="left", padx=50, pady=10)

        button4 = ttk.Button(frame2, text="Refresh", command=lambda: Refresh_data())
        button4.pack(side="left", padx=50, pady=10)

        #User should use Load_data() and Refresh_data()
        def Load_data(data_number):# Only used once at the beginning or in Refresh_data()
            header = Load_Column()
            GetDataFromNeo4j(header, data_number)
            tv1.bind('<ButtonRelease-1>', lambda event: tv1_click(event))
            for row in data_info:
                tv1.insert("", "end", values=row)
        def Refresh_data():
            data_info.clear()
            tv1.delete(*tv1.get_children())
            data_number = spinbox.get()
            Load_data(data_number)

        #User shouldn't touch these function
        def Load_Column():
            cypher_query = "MATCH (n:Node{deleted:False}) RETURN n LIMIT 1"
            result = graph.evaluate(cypher_query)
            header = []
            if result is None:
                pass
            else:
                result = graph.run(cypher_query)
                for record in result:
                    node = record['n']
                    properties = dict(node)
                    header= [attr for attr in properties if not callable(properties[attr])\
                             and not attr.startswith("__") and not attr.startswith("isNew")\
                             and not attr.startswith("time") and not attr.startswith("deleted")]
            #new columns
            tv1["columns"] = header
            for column in header:
                tv1.heading(column, text=column, command=lambda col=column: treeview_sort_column(tv1, col, False))
                #tv1.heading(column, text=column)
                tv1.column(column, width=50)
            return header
        def GetDataFromNeo4j(header, data_number):
            # 編寫 Cypher 查詢以檢索所有節點
            cypher_query = "MATCH (n:Node{deleted:False}) RETURN n limit " + str(data_number)
            # 執行 Cypher 查詢
            result = graph.run(cypher_query)
            # 遍歷結果並列印節點的屬性訊息
            for record in result:
                node = record["n"]
                # print(node)
                properties = dict(node)
                new_data = [properties[attr] for attr in header if not callable(properties[attr])\
                             and not attr.startswith("__") and not attr.startswith("isNew")\
                             and not attr.startswith("time") and not attr.startswith("deleted")]
                if new_data not in data_info:
                    data_info.append(new_data)

        Load_data(2500)
        init_trigger()

def Clear_Exist_Database():
    #clear all
    result = graph.run("""CALL apoc.periodic.iterate(
                        'MATCH (n) RETURN id(n) AS id', 
                        'MATCH (n) WHERE id(n)=id SET n.deleted = True', 
                        {batchSize: 1000})""")
#deleted nodes
class PageOne(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        frame1 = tk.LabelFrame(self, frame_styles, text="deleted Data List")
        frame1.place(rely=0.2, relx=0.02, height=440, width=980)

        frame2 = tk.LabelFrame(self, frame_styles, text="Some Feature")
        frame2.place(rely=0.05, relx=0.02, height=60, width=980)

        # This is a treeview.
        tv1 = ttk.Treeview(frame1)
        tv1["show"] = "headings"  # removes empty column
        tv1.place(relheight=1, relwidth=0.995)
        treescroll = tk.Scrollbar(frame1)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")
        def tv1_click(event):
            item = tv1.selection()
            if item:
                sub_window = create_sub_window("詳細資訊",300,400)

                val = tv1.item(item, "value")
                if val and isinstance(val, tuple) and len(val) > 0:
                    self.result_text = scrolledtext.ScrolledText(sub_window, width=60, height=10)
                    self.result_text.pack(padx=10, pady=10, fill="both", expand=True, side="bottom")
                    # 在初始化部分加入tag設定
                    self.result_text.tag_configure("tag_center", justify='center')
                    self.result_text.tag_configure("tag_indent", lmargin1=20)
                    # 獲取TreeView的列標題
                    columns = tv1["columns"]
                    # 生成Cypher查詢的字符串
                    exclude_columns = ['deleted', 'Cnt', 'PageRank', 'Label_Propagation', 'Degree_Centrality', 'WCC', 'lifetime']
                    values_str = ', '.join([f'{column}: "{value}"' for column, value in zip(columns, val)\
                                             if column != 'isNew' and column not in exclude_columns])

                    cypher_query = "MATCH (n:Node { " + values_str + " ,deleted:True}) RETURN n"
                    cypher_query2_1 = "MATCH (n:Node { " + values_str + " ,deleted:True})-[:INTERACTS_WITH]->(neighbor:Node{deleted:True})\
                                         RETURN count(neighbor)"
                    cypher_query2_2 = "MATCH (n:Node { " + values_str + " ,deleted:True})<-[:INTERACTS_WITH]-(neighbor:Node{deleted:True})\
                                         RETURN count(neighbor)"
                    cypher_query3_1 = "MATCH (n:Node { " + values_str + " ,deleted:True})-[:INTERACTS_WITH]->(neighbor:Node{deleted:True})\
                                         RETURN neighbor"
                    cypher_query3_2 = "MATCH (n:Node { " + values_str + " ,deleted:True})<-[:INTERACTS_WITH]-(neighbor:Node{deleted:True})\
                                         RETURN neighbor"
                    result = graph.run(cypher_query)
                    result2_1 = graph.evaluate(cypher_query2_1)
                    result2_2 = graph.evaluate(cypher_query2_2)
                    result3_1 = graph.run(cypher_query3_1)
                    result3_2 = graph.run(cypher_query3_2)
                    
                    # 顯示結果
                    for record in result:
                        node = record["n"]
                        properties = dict(node)
                        for key, value in properties.items():
                            if key != 'isNew' and key != 'time' and key != 'deleted':
                                self.result_text.insert(tk.END, f"{key}: {value}\n\n")
                        self.result_text.insert(tk.END, f"out degree: {result2_1}\n\n")
                        self.result_text.insert(tk.END, f"in degree: {result2_2}\n\n")
                        self.result_text.insert(tk.END, f"out neighbor:\n")
                        for node in result3_1:
                            node_data = node["neighbor"]
                            properties2 = dict(node_data)
                            new_data = {attr:properties2[attr] for attr in properties2 if not callable(properties2[attr])\
                                         and not attr.startswith("__") and not attr.startswith("isNew")\
                                         and not attr.startswith("time") and not attr.startswith("deleted")}
                            self.result_text.insert(tk.END, f"{new_data}\n")
                        self.result_text.insert(tk.END, f"\n")
                        self.result_text.insert(tk.END, f"in neighbor:\n")
                        for node in result3_2:
                            node_data = node["neighbor"]
                            properties2 = dict(node_data)
                            new_data = {attr:properties2[attr] for attr in properties2 if not callable(properties2[attr])\
                                         and not attr.startswith("__") and not attr.startswith("isNew")\
                                         and not attr.startswith("time") and not attr.startswith("deleted")}
                            self.result_text.insert(tk.END, f"{new_data}\n")
                        self.result_text.insert(tk.END, f"\n")
                        if 'time' in properties:
                            self.result_text.insert(tk.END, "time:\n")
                            timestamps = properties['time']
                            for timestamp in timestamps:
                                if timestamp == ',':
                                    self.result_text.insert(tk.END, f"\n")
                                else:
                                    self.result_text.insert(tk.END, f"{timestamp}")
                else:
                    print("No value found in the selected item.")
            selected_item = tv1.focus()
            if selected_item:
                # 如果有選取的行，取消選取
                tv1.selection_remove(selected_item)

        
        def on_sub_window_dataset_close():
            global sub_window_dataset

            # 子視窗關閉時清空
            sub_window_dataset.destroy()
            sub_window_dataset = None

        button3 = tk.Button(frame2, text="clear", command=lambda: Clear_Deleted_data())
        button3.pack(side="left", padx=50, pady=10)


        values_num = [2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]

        spinbox = tk.Spinbox(frame2, values=values_num, width=6, state="normal")
        spinbox.pack(side="left", padx=50, pady=10)

        button4 = ttk.Button(frame2, text="Refresh", command=lambda: Refresh_data())
        button4.pack(side="left", padx=50, pady=10)

        Var1 = tk.IntVar()
        Var2 = tk.IntVar()

        ##刪除並自動重整
        def Clear_Deleted_data():
            Clear_Deleted_Database()
            Refresh_data()

        #User should use Load_data() and Refresh_data()
        def Load_data(data_number):# Only used once at the beginning or in Refresh_data()
            cypher_query = """MATCH (n:Node{deleted:True})
                            WITH n, split(n.time, ',') AS timestamps
                            // 取得日期部分
                            WITH n, [timestamp IN timestamps | apoc.text.regexGroups(timestamp, '.+?Z')[0][0]] AS cleanedTimestamps
                            // 將字串轉換為日期時間對象
                            WITH n, [timestamp IN cleanedTimestamps | datetime(timestamp)] AS dateTimes
                            // 計算時間差異
                            WITH n, duration.between(head(dateTimes), tail(dateTimes)[-1]) AS timeDifference
                            SET n.lifetime = timeDifference
                            """
            graph.run(cypher_query)
            header = Load_Column()
            GetDataFromNeo4j(header, data_number)
            tv1.bind('<ButtonRelease-1>', lambda event: tv1_click(event))
            for row in deleted_data_info:
                tv1.insert("", "end", values=row)
        def Refresh_data():
            deleted_data_info.clear()
            tv1.delete(*tv1.get_children())
            data_number = spinbox.get()
            Load_data(data_number)

        #User shouldn't touch these function
        def Load_Column():
            exclude_columns = ['deleted', 'PageRank', 'Label_Propagation', 'Degree_Centrality', 'WCC']
            cypher_query = "MATCH (n:Node{deleted:True}) RETURN n LIMIT 1"
            result = graph.evaluate(cypher_query)
            header = []
            if result is None:
                pass
            else:
                result = graph.run(cypher_query)
                for record in result:
                    node = record['n']
                    properties = dict(node)
                    header= [attr for attr in properties if not callable(properties[attr])\
                             and not attr.startswith("__") and not attr.startswith("isNew")\
                             and not attr.startswith("time") and not attr.startswith("deleted")\
                             and attr not in exclude_columns]
            #new columns
            tv1["columns"] = header
            for column in header:
                tv1.heading(column, text=column, command=lambda col=column: treeview_sort_column(tv1, col, False))
                #tv1.heading(column, text=column)
                tv1.column(column, width=50)
            return header
        def GetDataFromNeo4j(header, data_number):
            # 編寫 Cypher 查詢以檢索所有節點
            cypher_query = "MATCH (n:Node{deleted:True}) RETURN n limit " + str(data_number)
            # 執行 Cypher 查詢
            result = graph.run(cypher_query)
            # 遍歷結果並列印節點的屬性訊息
            for record in result:
                node = record["n"]
                properties = dict(node)
                new_data = [properties[attr] for attr in header if not callable(properties[attr])\
                             and not attr.startswith("__") and not attr.startswith("isNew")\
                             and not attr.startswith("time") and not attr.startswith("deleted")]
                if new_data not in deleted_data_info:
                    deleted_data_info.append(new_data)
        Load_data(2500)

def Clear_Deleted_Database():
    #clear all
    result = graph.run("""CALL apoc.periodic.iterate(
                        'MATCH (n:Node{deleted:True})-[r]->() RETURN id(r) AS id', 
                        'MATCH (n:Node{deleted:True})-[r]->() WHERE id(r)=id DELETE r', 
                        {batchSize: 1000})""")
    result = graph.run("""CALL apoc.periodic.iterate(
                        'MATCH (n:Node{deleted:True})<-[r]-() RETURN id(r) AS id', 
                        'MATCH (n:Node{deleted:True})<-[r]-() WHERE id(r)=id DELETE r', 
                        {batchSize: 1000})""")
    result = graph.run("""CALL apoc.periodic.iterate(
                        'MATCH (n:Node{deleted:True}) RETURN id(n) AS id', 
                        'MATCH (n:Node{deleted:True}) WHERE id(n)=id DELETE n', 
                        {batchSize: 1000})""")
    


class PageThree(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Three")
        label1.pack(side="top")


class PageFour(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Four")
        label1.pack(side="top")


class PageTwo(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.LabelFrame(self, frame_styles, text="Command input")
        label1.place(rely=0.05, relx=0.02, height=530, width=980)
        
        
        # 文本框（用於顯示查詢結果）
        self.result_text = scrolledtext.ScrolledText(label1, width=60, height=10)
        self.result_text.pack(padx=10, pady=10, fill="both", expand=True ,side="bottom")

        # 輸入框
        self.query_entry = tk.Entry(label1, width=50)
        self.query_entry.pack(padx=10, pady=10, fill="x", expand=False ,side="top")
        self.query_entry.bind("<Return>", lambda event: self.run_query())

        # 按鈕
        self.query_button = tk.Button(label1, text="執行指令", command=self.run_query)
        self.query_button.pack(padx=10, pady=10, fill="x", expand=False ,side="right")

        # 清空按鈕
        self.clear_button = tk.Button(label1, text="清空輸入", command=self.clear_input)
        self.clear_button.pack(padx=10, pady=10, fill="x", expand=False ,side="top")   

    def run_query(self):

        query = self.query_entry.get()

        try:
            # 執行查詢
            result = graph.run(query)

            # 限制顯示的行數
            max_display_lines = 50
            displayed_lines = [f"{record}\n" for record in result.data()[:max_display_lines]]
            displayed_lines.append("... (結果過多時，僅會顯示前50行!!)\n")

            self.result_text.delete(1.0, tk.END) # 清空文本框
            self.result_text.insert(tk.END, "".join(displayed_lines))
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"錯誤: {e}")

    def clear_input(self):
        # 清空輸入框
        self.query_entry.delete(0, tk.END)


# class OpenNewWindow(tk.Tk):

#     def __init__(self, *args, **kwargs):

#         tk.Tk.__init__(self, *args, **kwargs)

#         main_frame = tk.Frame(self)
#         main_frame.pack_propagate(0)
#         main_frame.pack(fill="both", expand="true")
#         main_frame.grid_rowconfigure(0, weight=1)
#         main_frame.grid_columnconfigure(0, weight=1)
#         self.title("Here is the Title of the Window")
#         self.geometry("500x500")
#         self.resizable(0, 0)

#         frame1 = ttk.LabelFrame(main_frame, text="This is a ttk LabelFrame")
#         frame1.pack(expand=True, fill="both")

#         label1 = tk.Label(frame1, font=("Verdana", 20), text="OpenNewWindow Page")
#         label1.pack(side="top")


class OpenNewWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.title("About")

        # 獲取主頁大小和位置來計算視窗的位置
        xt = 250
        yt = 150
        root_x = root.winfo_x()
        root_y = root.winfo_y()

        root_width = root.winfo_width()
        root_height = root.winfo_height()

        x = root_x + (root_width - xt) // 2
        y = root_y + (root_height - yt) // 2
        self.geometry(f"{xt}x{yt}+{x}+{y}")

        self.resizable(0, 0)

        frame1 = ttk.LabelFrame(main_frame, text="關於本程式")
        frame1.pack(expand=True, fill="both")

        label1 = tk.Label(frame1, font=("Verdana", 9), text="Date analysis - Liifetime Tool")
        label1.pack(side="top", pady=10)

        label2 = tk.Label(frame1, font=("Verdana", 9), text="最後更新 2023/12/14")
        label2.pack(side="bottom")

        link_label = ttk.Label(frame1, font=("Verdana", 9), text="我們的Github頁面", cursor="hand2", padding=(0, 10), foreground="blue")
        link_label.pack(side="top")
        link_label.bind("<Button-1>", self.open_link)

        label3 = tk.Label(frame1, font=("Verdana", 9), text="作者 abyss & yochen")
        label3.pack(side="bottom")


    def open_link(self, event):
        # 典籍打開連結
        webbrowser.open("https://github.com/yochen729/graph_life_time_tool")

def create_sub_window(title,xt,yt):
    sub_window = tk.Toplevel(root)
    sub_window.title(title)

    # 獲取主頁大小和位置來計算子視窗的位置
    root_x = root.winfo_x()
    root_y = root.winfo_y()

    root_width = root.winfo_width()
    root_height = root.winfo_height()

    x = root_x + (root_width - xt) // 2
    y = root_y + (root_height - yt) // 2

    # 設置子視窗的大小和位置
    sub_window.geometry(f"{xt}x{yt}+{x}+{y}")
    return sub_window


top = WelcomePage()
top.title("Date analysis - Welcome Page")

root = MyApp()
root.withdraw()
root.title("Date analysis - Liifetime Tool")
root.minsize(1024, 600)
root.resizable(0, 0)

# 獲取螢幕寬度和高度
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

## 計算與設定歡迎頁的位置
window_width_welecome = 626
window_height_welecome = 431
x = (screen_width - window_width_welecome) // 2
y = (screen_height - window_height_welecome) // 2

top.geometry(f"{window_width_welecome}x{window_height_welecome}+{x}+{y}")
####

## 計算與設定主頁的位置
window_width = 1024
window_height = 600
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
####

sub_window_dataset = None
sub_window_algorithm = None
sub_window_search = None

root.mainloop()