import tkinter as tk
import csv
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
import time

from py2neo import Graph, Node, Relationship, walk, NodeMatcher, RelationshipMatcher, Subgraph
graph = Graph("bolt://localhost:7687", auth=("neo4j", "yooooooo"))


#data_info = [['Bulbasaur', 'Grass', '318'], ['Ivysaur', 'Grass', '405'], ['Venusaur', 'Grass', '525'], ['Charmander', 'Fire', '309'], ['Charmeleon', 'Fire', '405'], ['Charizard', 'Fire', '534'], ['Squirtle', 'Water', '314'], ['Wartortle', 'Water', '405'], ['Blastoise', 'Water', '530'], ['Caterpie', 'Bug', '195'], ['Metapod', 'Bug', '205'], ['Butterfree', 'Bug', '395'], ['Weedle', 'Bug', '195'], ['Kakuna', 'Bug', '205'], ['Beedrill', 'Bug', '395'], ['Pidgey', 'Normal', '251'], ['Pidgeotto', 'Normal', '349'], ['Pidgeot', 'Normal', '479'], ['Rattata', 'Normal', '253'], ['Raticate', 'Normal', '413'], ['Spearow', 'Normal', '262'], ['Fearow', 'Normal', '442'], ['Ekans', 'Poison', '288'], ['Arbok', 'Poison', '448'], ['Pikachu', 'Electric', '320'], ['Raichu', 'Electric', '485'], ['Sandshrew', 'Ground', '300'], ['Sandslash', 'Ground', '450'], ['Nidoran?', 'Poison', '275'], ['Nidorina', 'Poison', '365'], ['Nidoqueen', 'Poison', '505'], ['Nidoran?', 'Poison', '273'], ['Nidorino', 'Poison', '365'], ['Nidoking', 'Poison', '505'], ['Clefairy', 'Fairy', '323'], ['Clefable', 'Fairy', '483'], ['Vulpix', 'Fire', '299'], ['Ninetales', 'Fire', '505'], ['Jigglypuff', 'Normal', '270'], ['Wigglytuff', 'Normal', '435'], ['Zubat', 'Poison', '245'], ['Golbat', 'Poison', '455'], ['Oddish', 'Grass', '320'], ['Gloom', 'Grass', '395'], ['Vileplume', 'Grass', '490'], ['Paras', 'Bug', '285'], ['Parasect', 'Bug', '405'], ['Venonat', 'Bug', '305'], ['Venomoth', 'Bug', '450'], ['Diglett', 'Ground', '265'], ['Dugtrio', 'Ground', '425'], ['Meowth', 'Normal', '290'], ['Persian', 'Normal', '440'], ['Psyduck', 'Water', '320'], ['Golduck', 'Water', '500'], ['Mankey', 'Fighting', '305'], ['Primeape', 'Fighting', '455'], ['Growlithe', 'Fire', '350'], ['Arcanine', 'Fire', '555'], ['Poliwag', 'Water', '300'], ['Poliwhirl', 'Water', '385'], ['Poliwrath', 'Water', '510'], ['Abra', 'Psychic', '310'], ['Kadabra', 'Psychic', '400'], ['Alakazam', 'Psychic', '500'], ['Machop', 'Fighting', '305'], ['Machoke', 'Fighting', '405'], ['Machamp', 'Fighting', '505'], ['Bellsprout', 'Grass', '300'], ['Weepinbell', 'Grass', '390'], ['Victreebel', 'Grass', '490'], ['Tentacool', 'Water', '335'], ['Tentacruel', 'Water', '515'], ['Geodude', 'Rock', '300'], ['Graveler', 'Rock', '390'], ['Golem', 'Rock', '495'], ['Ponyta', 'Fire', '410'], ['Rapidash', 'Fire', '500'], ['Slowpoke', 'Water', '315'], ['Slowbro', 'Water', '490'], ['Magnemite', 'Electric', '325'], ['Magneton', 'Electric', '465'], ["Farfetch'd", 'Normal', '377'], ['Doduo', 'Normal', '310'], ['Dodrio', 'Normal', '470'], ['Seel', 'Water', '325'], ['Dewgong', 'Water', '475'], ['Grimer', 'Poison', '325'], ['Muk', 'Poison', '500'], ['Shellder', 'Water', '305'], ['Cloyster', 'Water', '525'], ['Gastly', 'Ghost', '310'], ['Haunter', 'Ghost', '405'], ['Gengar', 'Ghost', '500'], ['Onix', 'Rock', '385'], ['Drowzee', 'Psychic', '328'], ['Hypno', 'Psychic', '483'], ['Krabby', 'Water', '325'], ['Kingler', 'Water', '475'], ['Voltorb', 'Electric', '330'], ['Electrode', 'Electric', '490'], ['Exeggcute', 'Grass', '325'], ['Exeggutor', 'Grass', '530'], ['Cubone', 'Ground', '320'], ['Marowak', 'Ground', '425'], ['Hitmonlee', 'Fighting', '455'], ['Hitmonchan', 'Fighting', '455'], ['Lickitung', 'Normal', '385'], ['Koffing', 'Poison', '340'], ['Weezing', 'Poison', '490'], ['Rhyhorn', 'Ground', '345'], ['Rhydon', 'Ground', '485'], ['Chansey', 'Normal', '450'], ['Tangela', 'Grass', '435'], ['Kangaskhan', 'Normal', '490'], ['Horsea', 'Water', '295'], ['Seadra', 'Water', '440'], ['Goldeen', 'Water', '320'], ['Seaking', 'Water', '450'], ['Staryu', 'Water', '340'], ['Starmie', 'Water', '520'], ['Scyther', 'Bug', '500'], ['Jynx', 'Ice', '455'], ['Electabuzz', 'Electric', '490'], ['Magmar', 'Fire', '495'], ['Pinsir', 'Bug', '500'], ['Tauros', 'Normal', '490'], ['Magikarp', 'Water', '200'], ['Gyarados', 'Water', '540'], ['Lapras', 'Water', '535'], ['Ditto', 'Normal', '288'], ['Eevee', 'Normal', '325'], ['Vaporeon', 'Water', '525'], ['Jolteon', 'Electric', '525'], ['Flareon', 'Fire', '525'], ['Porygon', 'Normal', '395'], ['Omanyte', 'Rock', '355'], ['Omastar', 'Rock', '495'], ['Kabuto', 'Rock', '355'], ['Kabutops', 'Rock', '495'], ['Aerodactyl', 'Rock', '515'], ['Snorlax', 'Normal', '540'], ['Articuno', 'Ice', '580'], ['Zapdos', 'Electric', '580'], ['Moltres', 'Fire', '580'], ['Dratini', 'Dragon', '300'], ['Dragonair', 'Dragon', '420'], ['Dragonite', 'Dragon', '600'], ['Mewtwo', 'Psychic', '680'], ['Mew', 'Psychic', '600']]
data_info = []

frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#BEB2A7",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}
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

    l = [(convert(tv.set(k, col)), k) for k in tv.get_children('')]
    #i = cols.index(col)

    #l.sort(key=lambda t: t[i], reverse=reverse)
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col,command=lambda: treeview_sort_column(tv, col, not reverse))

def create_node_cypher(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
    headerNum = len(header)

    # 初始化 Cypher 查詢字串
    cypher_query = f"LOAD CSV WITH HEADERS FROM 'file:///{filename}' AS row\n"
    cypher_query += "MERGE (n:Node {"
    # 遍歷每個列標題，並建立 Cypher 查詢字串
    for index, column in enumerate(header):
        # 取得列標題
        column_name = column.strip()
        # 將列標題新增至 Cypher 查詢字串，格式為 "column_name: row.column_name"
        cypher_query += f"{column_name}: row.{column_name}"
        # 如果不是最後一個列標題，新增逗號分隔符
        if index < headerNum - 1:
            cypher_query += ", "
    cypher_query += "})"
    # 回傳 Cypher 查詢字串和 header
    return cypher_query, header

def create_relation_cypher(filename, id_name):
    # Read the header from the CSV file
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

    # Initialize Cypher query
    cypher_query = f"LOAD CSV WITH HEADERS FROM 'file:///{filename}' AS row\n"
    # Create relationship Cypher query
    cypher_query += f"MATCH (p1:Node {{{id_name}: row.{header[0]}}})\n"
    cypher_query += f"MATCH (p2:Node {{{id_name}: row.{header[1]}}})\n"
    cypher_query += "MERGE (p1)-[:INTERACTS_WITH]->(p2)\n"
    return cypher_query

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

        menu_orders = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu2", menu=menu_orders)

        menu_pricing = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu3", menu=menu_pricing)
        menu_pricing.add_command(label="Page One", command=lambda: parent.show_frame(PageOne))

        menu_operations = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu4", menu=menu_operations)
        menu_operations.add_command(label="Command Input", command=lambda: parent.show_frame(PageTwo))
        menu_positions = tk.Menu(menu_operations, tearoff=0)
        menu_operations.add_cascade(label="Menu5", menu=menu_positions)
        menu_positions.add_command(label="Page Three", command=lambda: parent.show_frame(PageThree))
        menu_positions.add_command(label="Page Four", command=lambda: parent.show_frame(PageFour))

        menu_help = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu6", menu=menu_help)
        menu_help.add_command(label="Open New Window", command=lambda: parent.OpenNewWindow())


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

        frame1 = tk.LabelFrame(self, frame_styles, text="Rough Data List")
        frame1.place(rely=0.2, relx=0.02, height=350, width=950)

        frame2 = tk.LabelFrame(self, frame_styles, text="Some Feature")
        frame2.place(rely=0.05, relx=0.02, height=60, width=950)

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
                sub_window = tk.Toplevel(root)
                sub_window.title("詳細資訊")
                # sub_window.geometry("300x400")

                #### 獲取主頁大小和位置來計算子視窗的位置
                root_x = root.winfo_x()
                root_y = root.winfo_y()

                root_width = root.winfo_width()
                root_height = root.winfo_height()

                x = root_x + (root_width - 300) // 2
                y = root_y + (root_height - 400) // 2

                # 設置子視窗的大小和位置
                sub_window.geometry(f"{300}x{400}+{x}+{y}")
                ######

                val = tv1.item(item, "value")
                if val and isinstance(val, tuple) and len(val) > 0:
                    first_value = val[0]
                    self.result_text = scrolledtext.ScrolledText(sub_window, width=60, height=10)
                    self.result_text.pack(padx=10, pady=10, fill="both", expand=True ,side="bottom")
                    self.result_text.insert(tk.END, first_value)
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
                sub_window_dataset = tk.Toplevel(root)
                sub_window_dataset.title("選擇匯入的資料集")
                # sub_window_dataset.geometry("300x400")

                #### 獲取主頁大小和位置來計算子視窗的位置
                root_x = root.winfo_x()
                root_y = root.winfo_y()

                root_width = root.winfo_width()
                root_height = root.winfo_height()

                x = root_x + (root_width - 300) // 2
                y = root_y + (root_height - 400) // 2

                # 設置子視窗的大小和位置
                sub_window_dataset.geometry(f"{300}x{400}+{x}+{y}")
                ######


                # 加入標籤
                label = tk.Label(sub_window_dataset, text="Please choose the dataset to load", padx=10, pady=10)
                label.pack()

                # 加入按鈕
                button1 = tk.Button(sub_window_dataset, text="Yeast", command=lambda: load_yeast())
                button1.pack(side="top", pady=30)
                def load_yeast():
                    filename = 'yeast_nodes.csv'
                    filename2 = 'yeast_relation.csv'
                    cypher_query, header = create_node_cypher(filename)
                    cypher_query2 = create_relation_cypher(filename2, header[0])
                    Clear_Database()
                    result = graph.run(cypher_query)
                    result = graph.run(cypher_query2)
                    Refresh_data()

                
                button2 = tk.Button(sub_window_dataset, text="Dataset 2", command=lambda: on_button_click("Dataset 2"))
                button2.pack(side="top", pady=30)
                
                button3 = tk.Button(sub_window_dataset, text="Dataset 3", command=lambda: on_button_click("Dataset 3"))
                button3.pack(side="top", pady=30)
                
                button4 = tk.Button(sub_window_dataset, text="Dataset 4", command=lambda: on_button_click("Dataset 4"))
                button4.pack(side="top", pady=30)

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
                sub_window_algorithm = tk.Toplevel(root)
                sub_window_algorithm.title("選擇要使用的演算法")
                # sub_window_algorithm.geometry("300x400")

                # 加入標籤
                label = tk.Label(sub_window_algorithm, text="Please choose the algorithm to use", padx=10, pady=10)
                label.pack()

                #### 獲取主頁大小和位置來計算子視窗的位置
                root_x = root.winfo_x()
                root_y = root.winfo_y()

                root_width = root.winfo_width()
                root_height = root.winfo_height()

                x = root_x + (root_width - 300) // 2
                y = root_y + (root_height - 500) // 2

                # 設置子視窗的大小和位置
                sub_window_algorithm.geometry(f"{300}x{500}+{x}+{y}")
                ######

                # 創建核取方塊
                check_var = tk.IntVar(sub_window_algorithm)
                check_button = tk.Checkbutton(sub_window_algorithm, text="是否寫入結果至節點屬性", variable=check_var)
                check_button.pack(pady=10)

        #### Page Rank ####
                button1 = tk.Button(sub_window_algorithm, text="Page Rank", command=lambda: pagerank())
                button1.pack(side="top", pady=20)

                def pagerank():
                    cypher_query = "CALL gds.pageRank.stream('test', {maxiterations:10, concurrency:4}) YIELD nodeId, score"
                    create_graph()
                    #取得benchmark結果和時間
                    result, time_taken = algorithm_benchmark(cypher_query)

                    if check_var.get():
                        cypher_query = "CALL gds.pageRank.write('test', {writeProperty:'PageRank', maxiterations:10, concurrency:4})"
                        algorithm_benchmark(cypher_query)

                    clear_graph()

                    print("執行時間:", time_taken, "s")
                    # 結果顯示
                    # for record in result:
                    #     print(record)

        #### Label Propagation ####
                button1 = tk.Button(sub_window_algorithm, text="Label Propagation", command=lambda: labelpropagation())
                button1.pack(side="top", pady=20)

                def labelpropagation():
                    cypher_query = "CALL gds.labelPropagation.stream('test', {maxiterations:10, concurrency:4}) YIELD nodeId, communityId"
                    create_graph()
                    #取得benchmark結果和時間
                    result, time_taken = algorithm_benchmark(cypher_query)

                    if check_var.get():
                        cypher_query = "CALL gds.labelPropagation.write('test', {writeProperty:'Label Propagation', maxiterations:10, concurrency:4})"
                        algorithm_benchmark(cypher_query)

                    clear_graph()

                    print("執行時間:", time_taken, "s")
                    # 結果顯示
                    # for record in result:
                    #     print(record)

        #### Degree Centrality ####
                button1 = tk.Button(sub_window_algorithm, text="Degree Centrality", command=lambda: degreecentrality())
                button1.pack(side="top", pady=20)

                def degreecentrality():
                    cypher_query = "CALL gds.degree.stream('test', {relationshipWeightProperty:null, concurrency:4}) YIELD nodeId, score"
                    create_graph()
                    #取得benchmark結果和時間
                    result, time_taken = algorithm_benchmark(cypher_query)
                                        
                    if check_var.get():
                        cypher_query = "CALL gds.degree.write('test', {writeProperty:'Degree Centrality', relationshipWeightProperty:null, concurrency:4})"
                        algorithm_benchmark(cypher_query)

                    clear_graph()

                    print("執行時間:", time_taken, "s")
                    # 結果顯示
                    # for record in result:
                    #     print(record)

        #### Weakly Connected Components  ####
                button1 = tk.Button(sub_window_algorithm, text="Weakly Connected Components", command=lambda: wcc())
                button1.pack(side="top", pady=20)

                def wcc():
                    cypher_query = "CALL gds.wcc.stream('test', {concurrency:4}) YIELD nodeId, componentId"
                    create_graph()
                    #取得benchmark結果和時間
                    result, time_taken = algorithm_benchmark(cypher_query)
                                                            
                    if check_var.get():
                        cypher_query = "CALL gds.wcc.write('test', {writeProperty:'WCC',concurrency:4})"
                        algorithm_benchmark(cypher_query)

                    clear_graph()

                    print("執行時間:", time_taken, "s")
                    # 結果顯示
                    # for record in result:
                    #     print(record)

                button2 = tk.Button(sub_window_algorithm, text="Clear (除錯用)", command=lambda: clear_graph())
                button2.pack(side="top", pady=30)

                def create_graph():
                    cypher_query = "CALL gds.graph.create('test', 'Node' ,  'INTERACTS_WITH')"
                    graph.run(cypher_query)

                def clear_graph():
                    cypher_query = "CALL gds.graph.drop('test')"
                    graph.run(cypher_query)

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


        button3 = tk.Button(frame2, text="Search", command=lambda: Clear_Database())
        button3.pack(side="left", padx=50, pady=10)


        values_num = [2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]

        spinbox = tk.Spinbox(frame2, values=values_num, width=6, state="normal")
        spinbox.pack(side="left", padx=50, pady=10)

        button4 = ttk.Button(frame2, text="Refresh", command=lambda: Refresh_data())
        button4.pack(side="left", padx=50, pady=10)

        Var1 = tk.IntVar()
        Var2 = tk.IntVar()

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
            cypher_query = "MATCH (n) RETURN n LIMIT 1"
            result = graph.evaluate(cypher_query)
            header = []
            if result is None:
                pass
            else:
                result = graph.run(cypher_query)
                for record in result:
                    node = record['n']
                    properties = dict(node)
                    header= [attr for attr in properties if not callable(properties[attr]) and not attr.startswith("__") and not attr.startswith("isNew")]
            #new columns
            tv1["columns"] = header
            for column in header:
                tv1.heading(column, text=column, command=lambda col=column: treeview_sort_column(tv1, col, False))
                #tv1.heading(column, text=column)
                tv1.column(column, width=50)
            return header
        def GetDataFromNeo4j(header, data_number):
            # 編寫 Cypher 查詢以檢索所有節點
            cypher_query = "MATCH (n) RETURN n limit " + str(data_number)
            # 執行 Cypher 查詢
            result = graph.run(cypher_query)
            # 遍歷結果並列印節點的屬性訊息
            for record in result:
                node = record["n"]
                properties = dict(node)
                # print(properties)
                # print(header)
                # new_data = [properties[attr] for attr in properties if not callable(properties[attr]) and not attr.startswith("__") and not attr.startswith("isNew")]
                new_data = [properties[attr] for attr in header if not callable(properties[attr]) and not attr.startswith("__") and not attr.startswith("isNew")]
                if new_data not in data_info:
                    data_info.append(new_data)
        def Clear_Database():
            #clear all
            result = graph.run("""CALL apoc.periodic.iterate(
                                'MATCH ()-[r]->() RETURN id(r) AS id', 
                                'MATCH ()-[r]->() WHERE id(r)=id DELETE r', 
                                {batchSize: 1000})""")
            result = graph.run("""CALL apoc.periodic.iterate(
                                'MATCH (n) RETURN id(n) AS id', 
                                'MATCH (n) WHERE id(n)=id DELETE n', 
                                {batchSize: 1000})""")


        Load_data(2500)


class PageOne(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page One")
        label1.pack(side="top")


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


class OpenNewWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.title("Here is the Title of the Window")
        self.geometry("500x500")
        self.resizable(0, 0)

        frame1 = ttk.LabelFrame(main_frame, text="This is a ttk LabelFrame")
        frame1.pack(expand=True, fill="both")

        label1 = tk.Label(frame1, font=("Verdana", 20), text="OpenNewWindow Page")
        label1.pack(side="top")


top = WelcomePage()
top.title("App Template - Date analysis - Liifetime")

root = MyApp()
root.withdraw()
root.title("Date analysis - Liifetime TOOLS")
root.minsize(1024, 600)

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

root.mainloop()