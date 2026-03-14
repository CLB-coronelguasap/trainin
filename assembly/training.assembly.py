  0           RESUME                   0

  1           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              0 (random)
              STORE_NAME               0 (random)

  2           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              1 (tkinter)
              STORE_NAME               2 (tk)

  3           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('messagebox',))
              IMPORT_NAME              1 (tkinter)
              IMPORT_FROM              3 (messagebox)
              STORE_NAME               3 (messagebox)
              POP_TOP

  4           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              4 (os)
              STORE_NAME               4 (os)

  7           BUILD_LIST               0
              LOAD_CONST               9 (('Crunchy Taco', 'Chipotle Chicken Burrito', 'Crunchwrap Supreme', 'Nachos BellGrande', 'Soft Taco', 'Chicken Quesadilla', 'Mexican Pizza'))
              LIST_EXTEND              1
              STORE_NAME               5 (MENU_MAINS)

  8           BUILD_LIST               0
              LOAD_CONST              10 (('Pepsi', 'Diet Pepsi', 'Baja Blast', 'Mtn Dew', 'Strawberry Passionfruit Agua Refresca', 'Blue Raspberry Freeze'))
              LIST_EXTEND              1
              STORE_NAME               6 (MENU_DRINKS)

  9           BUILD_LIST               0
              LOAD_CONST              11 (('Cinnabon Delights', 'Fries', 'Beans and Rice', 'Beans and Cheese', 'Chips and Guac', 'Chips and Nacho Cheese'))
              LIST_EXTEND              1
              STORE_NAME               7 (MENU_SIDES)

 10           BUILD_LIST               0
              LOAD_CONST              12 (('Small', 'Medium', 'Large', 'Extra Large'))
              LIST_EXTEND              1
              STORE_NAME               8 (MENU_SIZES)

 11           BUILD_LIST               0
              LOAD_CONST              13 (('Verde Salsa', 'Mild', 'Hot', 'Fire', 'Diablo', 'Nacho Cheese', 'Sour Cream', 'Creamy Jalapeño', 'Chipotle', 'Guacamole', 'Avocado Ranch', 'Spicy Ranch', 'Red'))
              LIST_EXTEND              1
              STORE_NAME               9 (MENU_SAUCES)

 13           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST               3 (<code object TacoGame at 0x7f9a84370b30, file "training.py", line 13>)
              MAKE_FUNCTION
              LOAD_CONST               4 ('TacoGame')
              CALL                     2
              STORE_NAME              10 (TacoGame)

254           LOAD_CONST               5 (<code object start_training at 0x7f9a84343210, file "training.py", line 254>)
              MAKE_FUNCTION
              STORE_NAME              11 (start_training)

264           LOAD_NAME               12 (__name__)
              LOAD_CONST               6 ('__main__')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       78 (to L1)
              NOT_TAKEN

266           LOAD_NAME                2 (tk)
              LOAD_ATTR               26 (Tk)
              PUSH_NULL
              CALL                     0
              STORE_NAME              14 (root)

267           LOAD_NAME               14 (root)
              LOAD_ATTR               31 (title + NULL|self)
              LOAD_CONST               7 ('Taco Training Game')
              CALL                     1
              POP_TOP

268           LOAD_NAME               14 (root)
              LOAD_ATTR               33 (geometry + NULL|self)
              LOAD_CONST               8 ('800x600')
              CALL                     1
              POP_TOP

269           LOAD_NAME               11 (start_training)
              PUSH_NULL
              LOAD_NAME               14 (root)
              CALL                     1
              POP_TOP

270           LOAD_NAME               14 (root)
              LOAD_ATTR               35 (mainloop + NULL|self)
              CALL                     0
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE

264   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object TacoGame at 0x7f9a84370b30, file "training.py", line 13>:
  --           MAKE_CELL                0 (__classdict__)

  13           RESUME                   0
               LOAD_NAME                0 (__name__)
               STORE_NAME               1 (__module__)
               LOAD_CONST               0 ('TacoGame')
               STORE_NAME               2 (__qualname__)
               LOAD_SMALL_INT          13
               STORE_NAME               3 (__firstlineno__)
               LOAD_LOCALS
               STORE_DEREF              0 (__classdict__)

  14           LOAD_CONST               1 ('Main application class for the Taco Training Game.')
               STORE_NAME               4 (__doc__)

  16           LOAD_CONST               2 (<code object __init__ at 0x55935d3a0040, file "training.py", line 16>)
               MAKE_FUNCTION
               STORE_NAME               5 (__init__)

  34           LOAD_CONST               3 (<code object clear_main_frame at 0x7f9a84369e30, file "training.py", line 34>)
               MAKE_FUNCTION
               STORE_NAME               6 (clear_main_frame)

  39           LOAD_CONST               4 (<code object show_tutorial at 0x55935d41dbe0, file "training.py", line 39>)
               MAKE_FUNCTION
               STORE_NAME               7 (show_tutorial)

  68           LOAD_CONST               5 (<code object generate_random_order at 0x55935d4086c0, file "training.py", line 68>)
               MAKE_FUNCTION
               STORE_NAME               8 (generate_random_order)

  92           LOAD_CONST               6 (<code object start_game at 0x55935d432db0, file "training.py", line 92>)
               MAKE_FUNCTION
               STORE_NAME               9 (start_game)

 161           LOAD_CONST               7 (<code object update_tray_listbox at 0x7f9a84480c00, file "training.py", line 161>)
               MAKE_FUNCTION
               STORE_NAME              10 (update_tray_listbox)

 167           LOAD_CONST               8 (<code object add_item_to_tray at 0x7f9a84342f70, file "training.py", line 167>)
               MAKE_FUNCTION
               STORE_NAME              11 (add_item_to_tray)

 173           LOAD_CONST               9 (<code object remove_selected_item at 0x7f9a84094030, file "training.py", line 173>)
               MAKE_FUNCTION
               STORE_NAME              12 (remove_selected_item)

 181           LOAD_CONST              10 (<code object clear_menu_frame at 0x7f9a84369f70, file "training.py", line 181>)
               MAKE_FUNCTION
               STORE_NAME              13 (clear_menu_frame)

 186           LOAD_CONST              11 (<code object show_items_in_grid at 0x55935d3fd710, file "training.py", line 186>)
               MAKE_FUNCTION
               STORE_NAME              14 (show_items_in_grid)

 207           LOAD_CONST              12 (<code object show_main_category at 0x55935d3efc20, file "training.py", line 207>)
               MAKE_FUNCTION
               STORE_NAME              15 (show_main_category)

 214           LOAD_CONST              13 (<code object show_mains_menu at 0x7f9a84327210, file "training.py", line 214>)
               MAKE_FUNCTION
               STORE_NAME              16 (show_mains_menu)

 217           LOAD_CONST              14 (<code object show_drinks_menu at 0x7f9a84327340, file "training.py", line 217>)
               MAKE_FUNCTION
               STORE_NAME              17 (show_drinks_menu)

 220           LOAD_CONST              15 (<code object show_sides_main_menu at 0x55935d429d90, file "training.py", line 220>)
               MAKE_FUNCTION
               STORE_NAME              18 (show_sides_main_menu)

 227           LOAD_CONST              16 (<code object show_food_sides_menu at 0x7f9a843275a0, file "training.py", line 227>)
               MAKE_FUNCTION
               STORE_NAME              19 (show_food_sides_menu)

 230           LOAD_CONST              17 (<code object show_sauces_menu at 0x7f9a843276d0, file "training.py", line 230>)
               MAKE_FUNCTION
               STORE_NAME              20 (show_sauces_menu)

 234           LOAD_CONST              18 (<code object show_sizes_menu at 0x7f9a843430c0, file "training.py", line 234>)
               MAKE_FUNCTION
               STORE_NAME              21 (show_sizes_menu)

 240           LOAD_CONST              19 (<code object serve_order at 0x7f9a842f54d0, file "training.py", line 240>)
               MAKE_FUNCTION
               STORE_NAME              22 (serve_order)
               LOAD_CONST              20 (('current_tray_items', 'customer_photo', 'main_frame', 'menu_frame', 'root', 'target_order_requirements', 'tray_listbox'))
               STORE_NAME              23 (__static_attributes__)
               LOAD_FAST_BORROW         0 (__classdict__)
               STORE_NAME              24 (__classdictcell__)
               LOAD_CONST              21 (None)
               RETURN_VALUE

Disassembly of <code object __init__ at 0x55935d3a0040, file "training.py", line 16>:
 16           RESUME                   0

 17           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (root, self)
              STORE_ATTR               0 (root)

 20           BUILD_MAP                0
              LOAD_FAST_BORROW         0 (self)
              STORE_ATTR               1 (target_order_requirements)

 21           BUILD_LIST               0
              LOAD_FAST_BORROW         0 (self)
              STORE_ATTR               2 (current_tray_items)

 22           LOAD_CONST               0 (None)
              LOAD_FAST_BORROW         0 (self)
              STORE_ATTR               3 (customer_photo)

 25           LOAD_GLOBAL              8 (tk)
              LOAD_ATTR               10 (Frame)
              PUSH_NULL
              LOAD_FAST_BORROW         1 (root)
              CALL                     1
              LOAD_FAST_BORROW         0 (self)
              STORE_ATTR               6 (main_frame)

 28           LOAD_GLOBAL              8 (tk)
              LOAD_ATTR               10 (Frame)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               12 (main_frame)
              CALL                     1
              LOAD_FAST_BORROW         0 (self)
              STORE_ATTR               7 (menu_frame)

 29           LOAD_GLOBAL              8 (tk)
              LOAD_ATTR               16 (Listbox)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               12 (main_frame)
              CALL                     1
              LOAD_FAST_BORROW         0 (self)
              STORE_ATTR               9 (tray_listbox)

 30           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               12 (main_frame)
              LOAD_ATTR               21 (pack + NULL|self)
              LOAD_GLOBAL              8 (tk)
              LOAD_ATTR               22 (BOTH)
              LOAD_CONST               1 (True)
              LOAD_CONST               2 (('fill', 'expand'))
              CALL_KW                  2
              POP_TOP

 32           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               25 (show_tutorial + NULL|self)
              CALL                     0
              POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object clear_main_frame at 0x7f9a84369e30, file "training.py", line 34>:
 34           RESUME                   0

 36           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (main_frame)
              LOAD_ATTR                3 (winfo_children + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER                19 (to L2)
              STORE_FAST               1 (widget)

 37           LOAD_FAST_BORROW         1 (widget)
              LOAD_ATTR                5 (destroy + NULL|self)
              CALL                     0
              POP_TOP
              JUMP_BACKWARD           21 (to L1)

 36   L2:     END_FOR
              POP_ITER
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object show_tutorial at 0x55935d41dbe0, file "training.py", line 39>:
 39           RESUME                   0

 41           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                1 (clear_main_frame + NULL|self)
              CALL                     0
              POP_TOP

 43           LOAD_GLOBAL              2 (tk)
              LOAD_ATTR                4 (Frame)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                6 (main_frame)
              LOAD_SMALL_INT          20
              LOAD_SMALL_INT          20
              LOAD_CONST               1 (('padx', 'pady'))
              CALL_KW                  3
              STORE_FAST               1 (tutorial_frame)

 44           LOAD_FAST_BORROW         1 (tutorial_frame)
              LOAD_ATTR                9 (pack + NULL|self)
              LOAD_CONST               2 (True)
              LOAD_CONST               3 (('expand',))
              CALL_KW                  1
              POP_TOP

 46           LOAD_GLOBAL              2 (tk)
              LOAD_ATTR               10 (Label)
              PUSH_NULL
              LOAD_FAST_BORROW         1 (tutorial_frame)
              LOAD_CONST               4 ('Taco Training Game - Tutorial')
              LOAD_CONST              14 (('Helvetica', 18, 'bold'))
              LOAD_CONST               5 (('text', 'font'))
              CALL_KW                  3
              STORE_FAST               2 (title_label)

 47           LOAD_FAST_BORROW         2 (title_label)
              LOAD_ATTR                9 (pack + NULL|self)
              LOAD_SMALL_INT          10
              LOAD_CONST               6 (('pady',))
              CALL_KW                  1
              POP_TOP

 50           LOAD_CONST               7 ("Welcome to the Taco Training!\n\nHere is how to play:\n1. Read the customer's order ticket on the screen.\n2. Use the 'Menus' below to build the order.\n   (Ordering -> Mains, Drinks, Sides, Sauces)\n3. Select sizes when prompted (e.g., Sides > Fries > Large).\n4. Your prepared items will appear in your 'Current Tray'.\n5. If you make a mistake, select the item in the tray and click 'Remove'.\n6. Once the tray perfectly matches the order, click 'Serve Order'.\n\nGood luck!")

 49           STORE_FAST               3 (instructions)

 62           LOAD_GLOBAL              2 (tk)
              LOAD_ATTR               10 (Label)
              PUSH_NULL
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (tutorial_frame, instructions)
              LOAD_CONST              15 (('Helvetica', 12))
              LOAD_GLOBAL              2 (tk)
              LOAD_ATTR               12 (LEFT)
              LOAD_CONST               8 (('text', 'font', 'justify'))
              CALL_KW                  4
              STORE_FAST               4 (instructions_label)

 63           LOAD_FAST_BORROW         4 (instructions_label)
              LOAD_ATTR                9 (pack + NULL|self)
              LOAD_SMALL_INT          10
              LOAD_CONST               6 (('pady',))
              CALL_KW                  1
              POP_TOP

 65           LOAD_GLOBAL              2 (tk)
              LOAD_ATTR               14 (Button)
              PUSH_NULL
              LOAD_FAST_BORROW         1 (tutorial_frame)
              LOAD_CONST               9 ('Start Game')
              LOAD_CONST              16 (('Helvetica', 14))
              LOAD_CONST              10 ('#4caf50')
              LOAD_CONST              11 ('white')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               16 (start_game)
              LOAD_CONST              12 (('text', 'font', 'bg', 'fg', 'command'))
              CALL_KW                  6
              STORE_FAST               5 (start_button)

 66           LOAD_FAST_BORROW         5 (start_button)
              LOAD_ATTR                9 (pack + NULL|self)
              LOAD_SMALL_INT          20
              LOAD_CONST               6 (('pady',))
              CALL_KW                  1
              POP_TOP
              LOAD_CONST              13 (None)
              RETURN_VALUE

Disassembly of <code object generate_random_order at 0x55935d4086c0, file "training.py", line 68>:
 68           RESUME                   0

 70           BUILD_MAP                0
              LOAD_FAST_BORROW         0 (self)
              STORE_ATTR               0 (target_order_requirements)

 73           LOAD_GLOBAL              2 (random)
              LOAD_ATTR                4 (randint)
              PUSH_NULL
              LOAD_SMALL_INT           1
              LOAD_SMALL_INT           5
              CALL                     2
              STORE_FAST               1 (num_mains)

 74           LOAD_GLOBAL              2 (random)
              LOAD_ATTR                6 (choice)
              PUSH_NULL
              LOAD_GLOBAL              8 (MENU_MAINS)
              CALL                     1
              STORE_FAST               2 (main_item)

 75           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (target_order_requirements)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_FAST_BORROW         2 (main_item)
              LOAD_SMALL_INT           0
              CALL                     2
              LOAD_FAST_BORROW         1 (num_mains)
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (target_order_requirements)
              LOAD_FAST_BORROW         2 (main_item)
              STORE_SUBSCR

 78           LOAD_GLOBAL              2 (random)
              LOAD_ATTR                4 (randint)
              PUSH_NULL
              LOAD_SMALL_INT           1
              LOAD_SMALL_INT           2
              CALL                     2
              STORE_FAST               3 (num_drinks)

 79           LOAD_GLOBAL              2 (random)
              LOAD_ATTR                6 (choice)
              PUSH_NULL
              LOAD_GLOBAL             12 (MENU_SIZES)
              CALL                     1
              LOAD_CONST               1 (' ')
              BINARY_OP                0 (+)
              LOAD_GLOBAL              2 (random)
              LOAD_ATTR                6 (choice)
              PUSH_NULL
              LOAD_GLOBAL             14 (MENU_DRINKS)
              CALL                     1
              BINARY_OP                0 (+)
              STORE_FAST               4 (drink_item)

 80           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (target_order_requirements)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_FAST_BORROW         4 (drink_item)
              LOAD_SMALL_INT           0
              CALL                     2
              LOAD_FAST_BORROW         3 (num_drinks)
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (target_order_requirements)
              LOAD_FAST_BORROW         4 (drink_item)
              STORE_SUBSCR

 83           LOAD_GLOBAL              2 (random)
              LOAD_ATTR                4 (randint)
              PUSH_NULL
              LOAD_SMALL_INT           1
              LOAD_SMALL_INT           3
              CALL                     2
              STORE_FAST               5 (num_sides)

 84           LOAD_GLOBAL              2 (random)
              LOAD_ATTR                6 (choice)
              PUSH_NULL
              LOAD_GLOBAL             12 (MENU_SIZES)
              CALL                     1
              LOAD_CONST               1 (' ')
              BINARY_OP                0 (+)
              LOAD_GLOBAL              2 (random)
              LOAD_ATTR                6 (choice)
              PUSH_NULL
              LOAD_GLOBAL             16 (MENU_SIDES)
              CALL                     1
              BINARY_OP                0 (+)
              STORE_FAST               6 (side_item)

 85           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (target_order_requirements)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_FAST_BORROW         6 (side_item)
              LOAD_SMALL_INT           0
              CALL                     2
              LOAD_FAST_BORROW         5 (num_sides)
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (target_order_requirements)
              LOAD_FAST_BORROW         6 (side_item)
              STORE_SUBSCR

 88           LOAD_GLOBAL              2 (random)
              LOAD_ATTR                4 (randint)
              PUSH_NULL
              LOAD_SMALL_INT           1
              LOAD_SMALL_INT           2
              CALL                     2
              STORE_FAST               7 (num_sauces)

 89           LOAD_GLOBAL              2 (random)
              LOAD_ATTR                6 (choice)
              PUSH_NULL
              LOAD_GLOBAL             18 (MENU_SAUCES)
              CALL                     1
              LOAD_CONST               2 (' Sauce')
              BINARY_OP                0 (+)
              STORE_FAST               8 (sauce_item)

 90           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (target_order_requirements)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_FAST_BORROW         8 (sauce_item)
              LOAD_SMALL_INT           0
              CALL                     2
              LOAD_FAST_BORROW         7 (num_sauces)
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (target_order_requirements)
              LOAD_FAST_BORROW         8 (sauce_item)
              STORE_SUBSCR
              LOAD_CONST               3 (None)
              RETURN_VALUE

Disassembly of <code object start_game at 0x55935d432db0, file "training.py", line 92>:
  92            RESUME                   0

  94            LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR                1 (clear_main_frame + NULL|self)
                CALL                     0
                POP_TOP

  95            LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR                3 (generate_random_order + NULL|self)
                CALL                     0
                POP_TOP

  96            BUILD_LIST               0
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR               2 (current_tray_items)

  99            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR                8 (Frame)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               10 (main_frame)
                LOAD_SMALL_INT         200
                LOAD_CONST               1 ('#f0f0f0')
                LOAD_SMALL_INT           2
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               12 (GROOVE)
                LOAD_CONST               2 (('height', 'bg', 'bd', 'relief'))
                CALL_KW                  5
                STORE_FAST               1 (top_frame)

 100            LOAD_FAST_BORROW         1 (top_frame)
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               16 (X)
                LOAD_SMALL_INT          10
                LOAD_SMALL_INT          10
                LOAD_CONST               3 (('fill', 'padx', 'pady'))
                CALL_KW                  3
                POP_TOP

 103            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR                8 (Frame)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (top_frame)
                LOAD_CONST               4 ('white')
                LOAD_SMALL_INT           2
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               18 (SOLID)
                LOAD_CONST               5 (('bg', 'bd', 'relief'))
                CALL_KW                  4
                STORE_FAST               2 (image_frame)

 104            LOAD_FAST_BORROW         2 (image_frame)
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               20 (LEFT)
                LOAD_SMALL_INT          10
                LOAD_SMALL_INT          10
                LOAD_CONST               6 (('side', 'padx', 'pady'))
                CALL_KW                  3
                POP_TOP

 106            LOAD_CONST               7 (None)
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              11 (customer_photo)

 107            LOAD_GLOBAL             24 (os)
                LOAD_ATTR               26 (path)
                LOAD_ATTR               29 (dirname + NULL|self)
                LOAD_GLOBAL             24 (os)
                LOAD_ATTR               26 (path)
                LOAD_ATTR               31 (abspath + NULL|self)
                LOAD_GLOBAL             32 (__file__)
                CALL                     1
                CALL                     1
                STORE_FAST               3 (base_dir)

 108            LOAD_GLOBAL             24 (os)
                LOAD_ATTR               26 (path)
                LOAD_ATTR               35 (join + NULL|self)
                LOAD_FAST_BORROW         3 (base_dir)
                LOAD_CONST               8 ('assets')
                LOAD_CONST               9 ('images')
                LOAD_CONST              10 ('customer')
                CALL                     4
                STORE_FAST               4 (image_dir)

 110            LOAD_GLOBAL             24 (os)
                LOAD_ATTR               26 (path)
                LOAD_ATTR               37 (exists + NULL|self)
                LOAD_FAST_BORROW         4 (image_dir)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE      183 (to L8)
                NOT_TAKEN

 111            LOAD_GLOBAL             24 (os)
                LOAD_ATTR               38 (listdir)
                PUSH_NULL
                LOAD_FAST_BORROW         4 (image_dir)
                CALL                     1
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (file)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2
        L2:     FOR_ITER                43 (to L5)
                STORE_FAST_LOAD_FAST    85 (file, file)
                LOAD_ATTR               41 (lower + NULL|self)
                CALL                     0
                LOAD_ATTR               43 (endswith + NULL|self)
                LOAD_CONST              36 (('.png', '.gif'))
                CALL                     1
                TO_BOOL
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           41 (to L2)
        L4:     LOAD_FAST_BORROW         5 (file)
                LIST_APPEND              2
                JUMP_BACKWARD           45 (to L2)
        L5:     END_FOR
                POP_ITER
        L6:     STORE_FAST               6 (image_files)
                STORE_FAST               5 (file)

 112            LOAD_FAST_BORROW         6 (image_files)
                TO_BOOL
                POP_JUMP_IF_FALSE      100 (to L8)
                NOT_TAKEN

 113            NOP

 114    L7:     LOAD_GLOBAL             24 (os)
                LOAD_ATTR               26 (path)
                LOAD_ATTR               35 (join + NULL|self)
                LOAD_FAST_BORROW         4 (image_dir)
                LOAD_GLOBAL             44 (random)
                LOAD_ATTR               46 (choice)
                PUSH_NULL
                LOAD_FAST_BORROW         6 (image_files)
                CALL                     1
                CALL                     2
                STORE_FAST               7 (chosen_image_path)

 115            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               48 (PhotoImage)
                PUSH_NULL
                LOAD_FAST_BORROW         7 (chosen_image_path)
                LOAD_CONST              11 (('file',))
                CALL_KW                  1
                STORE_FAST               8 (original_img)

 116            LOAD_FAST_BORROW         8 (original_img)
                LOAD_ATTR               51 (subsample + NULL|self)
                LOAD_SMALL_INT           2
                LOAD_SMALL_INT           2
                CALL                     2
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              11 (customer_photo)

 120    L8:     LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               22 (customer_photo)
                TO_BOOL
                POP_JUMP_IF_FALSE       55 (to L9)
                NOT_TAKEN

 121            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               54 (Label)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (image_frame, self)
                LOAD_ATTR               22 (customer_photo)
                LOAD_CONST               4 ('white')
                LOAD_CONST              12 (('image', 'bg'))
                CALL_KW                  3
                STORE_FAST               9 (customer_image_label)

 122            LOAD_FAST_BORROW         9 (customer_image_label)
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_SMALL_INT           5
                LOAD_SMALL_INT           5
                LOAD_CONST              13 (('padx', 'pady'))
                CALL_KW                  2
                POP_TOP
                JUMP_FORWARD            46 (to L10)

 124    L9:     LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               54 (Label)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (image_frame)
                LOAD_CONST              14 ('Customer\nPhoto')
                LOAD_SMALL_INT          15
                LOAD_SMALL_INT           8
                LOAD_CONST              15 ('#ccc')
                LOAD_CONST              16 (('text', 'width', 'height', 'bg'))
                CALL_KW                  5
                STORE_FAST               9 (customer_image_label)

 125            LOAD_FAST_BORROW         9 (customer_image_label)
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_SMALL_INT           5
                LOAD_SMALL_INT           5
                LOAD_CONST              13 (('padx', 'pady'))
                CALL_KW                  2
                POP_TOP

 128   L10:     LOAD_GLOBAL              6 (tk)
                LOAD_ATTR                8 (Frame)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (top_frame)
                LOAD_CONST              17 ('#ffffe0')
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               18 (SOLID)
                LOAD_CONST               5 (('bg', 'bd', 'relief'))
                CALL_KW                  4
                STORE_FAST              10 (ticket_frame)

 129            LOAD_FAST_BORROW        10 (ticket_frame)
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               20 (LEFT)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               56 (BOTH)
                LOAD_CONST              18 (True)
                LOAD_SMALL_INT          10
                LOAD_SMALL_INT          10
                LOAD_CONST              19 (('side', 'fill', 'expand', 'padx', 'pady'))
                CALL_KW                  5
                POP_TOP

 130            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               54 (Label)
                PUSH_NULL
                LOAD_FAST_BORROW        10 (ticket_frame)
                LOAD_CONST              20 ('ORDER TICKET')
                LOAD_CONST              37 (('Helvetica', 12, 'bold'))
                LOAD_CONST              17 ('#ffffe0')
                LOAD_CONST              21 (('text', 'font', 'bg'))
                CALL_KW                  4
                LOAD_ATTR               15 (pack + NULL|self)
                CALL                     0
                POP_TOP

 132            LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               58 (target_order_requirements)
                LOAD_ATTR               61 (items + NULL|self)
                CALL                     0
                GET_ITER
       L11:     FOR_ITER                66 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  188 (item, count)

 133            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               54 (Label)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 172 (ticket_frame, count)
                FORMAT_SIMPLE
                LOAD_CONST              22 ('x ')
                LOAD_FAST_BORROW        11 (item)
                FORMAT_SIMPLE
                BUILD_STRING             3
                LOAD_CONST              38 (('Helvetica', 12))
                LOAD_CONST              17 ('#ffffe0')
                LOAD_CONST              21 (('text', 'font', 'bg'))
                CALL_KW                  4
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               62 (W)
                LOAD_SMALL_INT          20
                LOAD_CONST              23 (('anchor', 'padx'))
                CALL_KW                  2
                POP_TOP
                JUMP_BACKWARD           68 (to L11)

 132   L12:     END_FOR
                POP_ITER

 136            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR                8 (Frame)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               10 (main_frame)
                CALL                     1
                STORE_FAST              13 (bottom_frame)

 137            LOAD_FAST_BORROW        13 (bottom_frame)
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               56 (BOTH)
                LOAD_CONST              18 (True)
                LOAD_SMALL_INT          10
                LOAD_SMALL_INT          10
                LOAD_CONST              24 (('fill', 'expand', 'padx', 'pady'))
                CALL_KW                  4
                POP_TOP

 140            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               64 (LabelFrame)
                PUSH_NULL
                LOAD_FAST_BORROW        13 (bottom_frame)
                LOAD_CONST              25 ('Menu Operations')
                LOAD_CONST              39 (('Helvetica', 10, 'bold'))
                LOAD_CONST              26 (('text', 'font'))
                CALL_KW                  3
                STORE_FAST              14 (menu_container)

 141            LOAD_FAST_BORROW        14 (menu_container)
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               20 (LEFT)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               56 (BOTH)
                LOAD_CONST              18 (True)
                LOAD_CONST              40 ((0, 5))
                LOAD_CONST              27 (('side', 'fill', 'expand', 'padx'))
                CALL_KW                  4
                POP_TOP

 143            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR                8 (Frame)
                PUSH_NULL
                LOAD_FAST_BORROW        14 (menu_container)
                CALL                     1
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              33 (menu_frame)

 144            LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               66 (menu_frame)
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               56 (BOTH)
                LOAD_CONST              18 (True)
                LOAD_SMALL_INT           5
                LOAD_SMALL_INT           5
                LOAD_CONST              24 (('fill', 'expand', 'padx', 'pady'))
                CALL_KW                  4
                POP_TOP

 147            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               64 (LabelFrame)
                PUSH_NULL
                LOAD_FAST_BORROW        13 (bottom_frame)
                LOAD_CONST              28 ('Current Tray')
                LOAD_CONST              39 (('Helvetica', 10, 'bold'))
                LOAD_CONST              26 (('text', 'font'))
                CALL_KW                  3
                STORE_FAST              15 (tray_container)

 148            LOAD_FAST_BORROW        15 (tray_container)
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               68 (RIGHT)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               56 (BOTH)
                LOAD_CONST              18 (True)
                LOAD_CONST              41 ((5, 0))
                LOAD_CONST              27 (('side', 'fill', 'expand', 'padx'))
                CALL_KW                  4
                POP_TOP

 150            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               70 (Listbox)
                PUSH_NULL
                LOAD_FAST_BORROW        15 (tray_container)
                LOAD_CONST              42 (('Helvetica', 11))
                LOAD_CONST              29 (('font',))
                CALL_KW                  2
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              36 (tray_listbox)

 151            LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               72 (tray_listbox)
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               56 (BOTH)
                LOAD_CONST              18 (True)
                LOAD_SMALL_INT           5
                LOAD_SMALL_INT           5
                LOAD_CONST              24 (('fill', 'expand', 'padx', 'pady'))
                CALL_KW                  4
                POP_TOP

 153            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR                8 (Frame)
                PUSH_NULL
                LOAD_FAST_BORROW        15 (tray_container)
                CALL                     1
                STORE_FAST              16 (button_frame)

 154            LOAD_FAST_BORROW        16 (button_frame)
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               16 (X)
                LOAD_SMALL_INT           5
                LOAD_SMALL_INT           5
                LOAD_CONST               3 (('fill', 'padx', 'pady'))
                CALL_KW                  3
                POP_TOP

 156            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               74 (Button)
                PUSH_NULL
                LOAD_FAST_BORROW        16 (button_frame)
                LOAD_CONST              30 ('Remove Selected')
                LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               76 (remove_selected_item)
                LOAD_CONST              31 (('text', 'command'))
                CALL_KW                  3
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               20 (LEFT)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               16 (X)
                LOAD_CONST              18 (True)
                LOAD_CONST              32 (('side', 'fill', 'expand'))
                CALL_KW                  3
                POP_TOP

 157            LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               74 (Button)
                PUSH_NULL
                LOAD_FAST_BORROW        16 (button_frame)
                LOAD_CONST              33 ('SERVE ORDER')
                LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               78 (serve_order)
                LOAD_CONST              34 ('#2196F3')
                LOAD_CONST               4 ('white')
                LOAD_CONST              39 (('Helvetica', 10, 'bold'))
                LOAD_CONST              35 (('text', 'command', 'bg', 'fg', 'font'))
                CALL_KW                  6
                LOAD_ATTR               15 (pack + NULL|self)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               68 (RIGHT)
                LOAD_GLOBAL              6 (tk)
                LOAD_ATTR               16 (X)
                LOAD_CONST              18 (True)
                LOAD_CONST              41 ((5, 0))
                LOAD_CONST              27 (('side', 'fill', 'expand', 'padx'))
                CALL_KW                  4
                POP_TOP

 159            LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               81 (show_main_category + NULL|self)
                CALL                     0
                POP_TOP
                LOAD_CONST               7 (None)
                RETURN_VALUE

  --   L13:     SWAP                     2
                POP_TOP

 111            SWAP                     2
                STORE_FAST               5 (file)
                RERAISE                  0

  --   L14:     PUSH_EXC_INFO

 117            LOAD_GLOBAL             52 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L16)
                NOT_TAKEN
                POP_TOP

 118   L15:     POP_EXCEPT
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 964 (to L8)

 117   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L13 [2]
  L4 to L6 -> L13 [2]
  L7 to L8 -> L14 [0]
  L14 to L15 -> L17 [1] lasti
  L16 to L17 -> L17 [1] lasti

Disassembly of <code object update_tray_listbox at 0x7f9a84480c00, file "training.py", line 161>:
161           RESUME                   0

163           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (tray_listbox)
              LOAD_ATTR                3 (delete + NULL|self)
              LOAD_SMALL_INT           0
              LOAD_GLOBAL              4 (tk)
              LOAD_ATTR                6 (END)
              CALL                     2
              POP_TOP

164           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                8 (current_tray_items)
              GET_ITER
      L1:     FOR_ITER                45 (to L2)
              STORE_FAST               1 (item)

165           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (tray_listbox)
              LOAD_ATTR               11 (insert + NULL|self)
              LOAD_GLOBAL              4 (tk)
              LOAD_ATTR                6 (END)
              LOAD_FAST_BORROW         1 (item)
              CALL                     2
              POP_TOP
              JUMP_BACKWARD           47 (to L1)

164   L2:     END_FOR
              POP_ITER
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object add_item_to_tray at 0x7f9a84342f70, file "training.py", line 167>:
167           RESUME                   0

169           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (current_tray_items)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_FAST_BORROW         1 (item)
              CALL                     1
              POP_TOP

170           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                5 (update_tray_listbox + NULL|self)
              CALL                     0
              POP_TOP

171           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                7 (show_main_category + NULL|self)
              CALL                     0
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object remove_selected_item at 0x7f9a84094030, file "training.py", line 173>:
173           RESUME                   0

175           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (tray_listbox)
              LOAD_ATTR                3 (curselection + NULL|self)
              CALL                     0
              STORE_FAST               1 (selected_indices)

176           LOAD_FAST_BORROW         1 (selected_indices)
              TO_BOOL
              POP_JUMP_IF_FALSE       55 (to L1)
              NOT_TAKEN

177           LOAD_FAST_BORROW         1 (selected_indices)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              STORE_FAST               2 (item_index)

178           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                4 (current_tray_items)
              LOAD_ATTR                7 (pop + NULL|self)
              LOAD_FAST_BORROW         2 (item_index)
              CALL                     1
              POP_TOP

179           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                9 (update_tray_listbox + NULL|self)
              CALL                     0
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE

176   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object clear_menu_frame at 0x7f9a84369f70, file "training.py", line 181>:
181           RESUME                   0

183           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (menu_frame)
              LOAD_ATTR                3 (winfo_children + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER                19 (to L2)
              STORE_FAST               1 (widget)

184           LOAD_FAST_BORROW         1 (widget)
              LOAD_ATTR                5 (destroy + NULL|self)
              CALL                     0
              POP_TOP
              JUMP_BACKWARD           21 (to L1)

183   L2:     END_FOR
              POP_ITER
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object show_items_in_grid at 0x55935d3fd710, file "training.py", line 186>:
  --           MAKE_CELL                2 (click_callback)

 186           RESUME                   0

 188           LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                1 (clear_menu_frame + NULL|self)
               CALL                     0
               POP_TOP

 189           LOAD_GLOBAL              2 (tk)
               LOAD_ATTR                4 (Button)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                6 (menu_frame)
               LOAD_CONST               1 ('< Back')
               LOAD_FAST_BORROW         3 (back_command)
               LOAD_CONST               2 ('#ffcccc')
               LOAD_CONST               3 (('text', 'command', 'bg'))
               CALL_KW                  4
               LOAD_ATTR                9 (grid + NULL|self)
               LOAD_SMALL_INT           0
               LOAD_SMALL_INT           0
               LOAD_SMALL_INT           3
               LOAD_CONST               4 ('we')
               LOAD_SMALL_INT           5
               LOAD_SMALL_INT           5
               LOAD_CONST               5 (('row', 'column', 'columnspan', 'sticky', 'pady', 'padx'))
               CALL_KW                  6
               POP_TOP

 192           LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                6 (menu_frame)
               LOAD_ATTR               11 (columnconfigure + NULL|self)
               LOAD_SMALL_INT           0
               LOAD_SMALL_INT           1
               LOAD_CONST               6 (('weight',))
               CALL_KW                  2
               POP_TOP

 193           LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                6 (menu_frame)
               LOAD_ATTR               11 (columnconfigure + NULL|self)
               LOAD_SMALL_INT           1
               LOAD_SMALL_INT           1
               LOAD_CONST               6 (('weight',))
               CALL_KW                  2
               POP_TOP

 194           LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                6 (menu_frame)
               LOAD_ATTR               11 (columnconfigure + NULL|self)
               LOAD_SMALL_INT           2
               LOAD_SMALL_INT           1
               LOAD_CONST               6 (('weight',))
               CALL_KW                  2
               POP_TOP

 196           LOAD_SMALL_INT           1
               STORE_FAST               4 (row_index)

 197           LOAD_SMALL_INT           0
               STORE_FAST               5 (col_index)

 198           LOAD_FAST_BORROW         1 (item_list)
               GET_ITER
       L1:     FOR_ITER                92 (to L3)
               STORE_FAST               6 (item_name)

 199           LOAD_GLOBAL              2 (tk)
               LOAD_ATTR                4 (Button)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                6 (menu_frame)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 102 (item_name, item_name)
               BUILD_TUPLE              1
               LOAD_FAST_BORROW         2 (click_callback)
               BUILD_TUPLE              1
               LOAD_CONST               7 (<code object <lambda> at 0x7f9a843de100, file "training.py", line 199>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               LOAD_CONST               8 (('text', 'command'))
               CALL_KW                  3
               LOAD_ATTR                9 (grid + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (row_index, col_index)
               LOAD_CONST               4 ('we')
               LOAD_SMALL_INT           2
               LOAD_SMALL_INT           2
               LOAD_CONST               9 (('row', 'column', 'sticky', 'padx', 'pady'))
               CALL_KW                  5
               POP_TOP

 201           LOAD_FAST_BORROW         5 (col_index)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (col_index)

 203           LOAD_FAST_BORROW         5 (col_index)
               LOAD_SMALL_INT           2
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               JUMP_BACKWARD           81 (to L1)

 204   L2:     LOAD_SMALL_INT           0
               STORE_FAST               5 (col_index)

 205           LOAD_FAST_BORROW         4 (row_index)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               4 (row_index)
               JUMP_BACKWARD           94 (to L1)

 198   L3:     END_FOR
               POP_ITER
               LOAD_CONST              10 (None)
               RETURN_VALUE

Disassembly of <code object <lambda> at 0x7f9a843de100, file "training.py", line 199>:
  --           COPY_FREE_VARS           1

 199           RESUME                   0
               LOAD_DEREF               1 (click_callback)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (name)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object show_main_category at 0x55935d3efc20, file "training.py", line 207>:
207           RESUME                   0

209           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                1 (clear_menu_frame + NULL|self)
              CALL                     0
              POP_TOP

210           LOAD_GLOBAL              2 (tk)
              LOAD_ATTR                4 (Button)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                6 (menu_frame)
              LOAD_CONST               1 ('Ordering (Mains)')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                8 (show_mains_menu)
              LOAD_CONST               7 (('Helvetica', 12))
              LOAD_SMALL_INT           2
              LOAD_CONST               2 (('text', 'command', 'font', 'height'))
              CALL_KW                  5
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_GLOBAL              2 (tk)
              LOAD_ATTR               12 (X)
              LOAD_SMALL_INT           5
              LOAD_CONST               3 (('fill', 'pady'))
              CALL_KW                  2
              POP_TOP

211           LOAD_GLOBAL              2 (tk)
              LOAD_ATTR                4 (Button)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                6 (menu_frame)
              LOAD_CONST               4 ('Drinks')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               14 (show_drinks_menu)
              LOAD_CONST               7 (('Helvetica', 12))
              LOAD_SMALL_INT           2
              LOAD_CONST               2 (('text', 'command', 'font', 'height'))
              CALL_KW                  5
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_GLOBAL              2 (tk)
              LOAD_ATTR               12 (X)
              LOAD_SMALL_INT           5
              LOAD_CONST               3 (('fill', 'pady'))
              CALL_KW                  2
              POP_TOP

212           LOAD_GLOBAL              2 (tk)
              LOAD_ATTR                4 (Button)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                6 (menu_frame)
              LOAD_CONST               5 ('Sides & Sauces')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               16 (show_sides_main_menu)
              LOAD_CONST               7 (('Helvetica', 12))
              LOAD_SMALL_INT           2
              LOAD_CONST               2 (('text', 'command', 'font', 'height'))
              CALL_KW                  5
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_GLOBAL              2 (tk)
              LOAD_ATTR               12 (X)
              LOAD_SMALL_INT           5
              LOAD_CONST               3 (('fill', 'pady'))
              CALL_KW                  2
              POP_TOP
              LOAD_CONST               6 (None)
              RETURN_VALUE

Disassembly of <code object show_mains_menu at 0x7f9a84327210, file "training.py", line 214>:
214           RESUME                   0

215           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                1 (show_items_in_grid + NULL|self)
              LOAD_GLOBAL              2 (MENU_MAINS)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                4 (add_item_to_tray)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                6 (show_main_category)
              CALL                     3
              POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object show_drinks_menu at 0x7f9a84327340, file "training.py", line 217>:
  --           MAKE_CELL                0 (self)

 217           RESUME                   0

 218           LOAD_DEREF               0 (self)
               LOAD_ATTR                1 (show_items_in_grid + NULL|self)
               LOAD_GLOBAL              2 (MENU_DRINKS)
               LOAD_FAST_BORROW         0 (self)
               BUILD_TUPLE              1
               LOAD_CONST               0 (<code object <lambda> at 0x7f9a84442530, file "training.py", line 218>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               LOAD_DEREF               0 (self)
               LOAD_ATTR                4 (show_main_category)
               CALL                     3
               POP_TOP
               LOAD_CONST               1 (None)
               RETURN_VALUE

Disassembly of <code object <lambda> at 0x7f9a84442530, file "training.py", line 218>:
  --           COPY_FREE_VARS           1

 218           RESUME                   0
               LOAD_DEREF               1 (self)
               LOAD_ATTR                1 (show_sizes_menu + NULL|self)
               LOAD_FAST_BORROW         0 (drink)
               LOAD_CONST               0 ('drink')
               CALL                     2
               RETURN_VALUE

Disassembly of <code object show_sides_main_menu at 0x55935d429d90, file "training.py", line 220>:
220           RESUME                   0

222           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                1 (clear_menu_frame + NULL|self)
              CALL                     0
              POP_TOP

223           LOAD_GLOBAL              2 (tk)
              LOAD_ATTR                4 (Button)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                6 (menu_frame)
              LOAD_CONST               1 ('< Back')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                8 (show_main_category)
              LOAD_CONST               2 ('#ffcccc')
              LOAD_CONST               3 (('text', 'command', 'bg'))
              CALL_KW                  4
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_GLOBAL              2 (tk)
              LOAD_ATTR               12 (X)
              LOAD_SMALL_INT           5
              LOAD_CONST               4 (('fill', 'pady'))
              CALL_KW                  2
              POP_TOP

224           LOAD_GLOBAL              2 (tk)
              LOAD_ATTR                4 (Button)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                6 (menu_frame)
              LOAD_CONST               5 ('Food Sides')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               14 (show_food_sides_menu)
              LOAD_CONST               9 (('Helvetica', 12))
              LOAD_SMALL_INT           2
              LOAD_CONST               6 (('text', 'command', 'font', 'height'))
              CALL_KW                  5
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_GLOBAL              2 (tk)
              LOAD_ATTR               12 (X)
              LOAD_SMALL_INT           5
              LOAD_CONST               4 (('fill', 'pady'))
              CALL_KW                  2
              POP_TOP

225           LOAD_GLOBAL              2 (tk)
              LOAD_ATTR                4 (Button)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                6 (menu_frame)
              LOAD_CONST               7 ('Sauces')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               16 (show_sauces_menu)
              LOAD_CONST               9 (('Helvetica', 12))
              LOAD_SMALL_INT           2
              LOAD_CONST               6 (('text', 'command', 'font', 'height'))
              CALL_KW                  5
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_GLOBAL              2 (tk)
              LOAD_ATTR               12 (X)
              LOAD_SMALL_INT           5
              LOAD_CONST               4 (('fill', 'pady'))
              CALL_KW                  2
              POP_TOP
              LOAD_CONST               8 (None)
              RETURN_VALUE

Disassembly of <code object show_food_sides_menu at 0x7f9a843275a0, file "training.py", line 227>:
  --           MAKE_CELL                0 (self)

 227           RESUME                   0

 228           LOAD_DEREF               0 (self)
               LOAD_ATTR                1 (show_items_in_grid + NULL|self)
               LOAD_GLOBAL              2 (MENU_SIDES)
               LOAD_FAST_BORROW         0 (self)
               BUILD_TUPLE              1
               LOAD_CONST               0 (<code object <lambda> at 0x7f9a84442430, file "training.py", line 228>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               LOAD_DEREF               0 (self)
               LOAD_ATTR                4 (show_sides_main_menu)
               CALL                     3
               POP_TOP
               LOAD_CONST               1 (None)
               RETURN_VALUE

Disassembly of <code object <lambda> at 0x7f9a84442430, file "training.py", line 228>:
  --           COPY_FREE_VARS           1

 228           RESUME                   0
               LOAD_DEREF               1 (self)
               LOAD_ATTR                1 (show_sizes_menu + NULL|self)
               LOAD_FAST_BORROW         0 (side)
               LOAD_CONST               0 ('side')
               CALL                     2
               RETURN_VALUE

Disassembly of <code object show_sauces_menu at 0x7f9a843276d0, file "training.py", line 230>:
  --           MAKE_CELL                0 (self)

 230           RESUME                   0

 232           LOAD_DEREF               0 (self)
               LOAD_ATTR                1 (show_items_in_grid + NULL|self)
               LOAD_GLOBAL              2 (MENU_SAUCES)
               LOAD_FAST_BORROW         0 (self)
               BUILD_TUPLE              1
               LOAD_CONST               0 (<code object <lambda> at 0x7f9a84443e30, file "training.py", line 232>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               LOAD_DEREF               0 (self)
               LOAD_ATTR                4 (show_sides_main_menu)
               CALL                     3
               POP_TOP
               LOAD_CONST               1 (None)
               RETURN_VALUE

Disassembly of <code object <lambda> at 0x7f9a84443e30, file "training.py", line 232>:
  --           COPY_FREE_VARS           1

 232           RESUME                   0
               LOAD_DEREF               1 (self)
               LOAD_ATTR                1 (add_item_to_tray + NULL|self)
               LOAD_FAST_BORROW         0 (sauce)
               FORMAT_SIMPLE
               LOAD_CONST               0 (' Sauce')
               BUILD_STRING             2
               CALL                     1
               RETURN_VALUE

Disassembly of <code object show_sizes_menu at 0x7f9a843430c0, file "training.py", line 234>:
  --           MAKE_CELL                0 (self)
               MAKE_CELL                1 (base_item)

 234           RESUME                   0

 237           LOAD_FAST_BORROW         2 (category)
               LOAD_CONST               1 ('drink')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       13 (to L1)
               NOT_TAKEN
               LOAD_DEREF               0 (self)
               LOAD_ATTR                0 (show_drinks_menu)
               JUMP_FORWARD            11 (to L2)
       L1:     LOAD_DEREF               0 (self)
               LOAD_ATTR                2 (show_food_sides_menu)
       L2:     STORE_FAST               3 (back_cmd)

 238           LOAD_DEREF               0 (self)
               LOAD_ATTR                5 (show_items_in_grid + NULL|self)
               LOAD_GLOBAL              6 (MENU_SIZES)
               LOAD_FAST_BORROW         1 (base_item)
               LOAD_FAST_BORROW         0 (self)
               BUILD_TUPLE              2
               LOAD_CONST               2 (<code object <lambda> at 0x7f9a84442730, file "training.py", line 238>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               LOAD_FAST_BORROW         3 (back_cmd)
               CALL                     3
               POP_TOP
               LOAD_CONST               3 (None)
               RETURN_VALUE

Disassembly of <code object <lambda> at 0x7f9a84442730, file "training.py", line 238>:
  --           COPY_FREE_VARS           2

 238           RESUME                   0
               LOAD_DEREF               2 (self)
               LOAD_ATTR                1 (add_item_to_tray + NULL|self)
               LOAD_FAST_BORROW         0 (size_option)
               FORMAT_SIMPLE
               LOAD_CONST               0 (' ')
               LOAD_DEREF               1 (base_item)
               FORMAT_SIMPLE
               BUILD_STRING             3
               CALL                     1
               RETURN_VALUE

Disassembly of <code object serve_order at 0x7f9a842f54d0, file "training.py", line 240>:
240           RESUME                   0

242           BUILD_MAP                0
              STORE_FAST               1 (tray_counts)

244           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (current_tray_items)
              GET_ITER
      L1:     FOR_ITER                30 (to L2)
              STORE_FAST               2 (item)

245           LOAD_FAST_BORROW         1 (tray_counts)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_FAST_BORROW         2 (item)
              LOAD_SMALL_INT           0
              CALL                     2
              LOAD_SMALL_INT           1
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (tray_counts, item)
              STORE_SUBSCR
              JUMP_BACKWARD           32 (to L1)

244   L2:     END_FOR
              POP_ITER

248           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (tray_counts, self)
              LOAD_ATTR                4 (target_order_requirements)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       42 (to L3)
              NOT_TAKEN

249           LOAD_GLOBAL              6 (messagebox)
              LOAD_ATTR                8 (showinfo)
              PUSH_NULL
              LOAD_CONST               1 ('Success')
              LOAD_CONST               2 ('Perfect! The customer is happy.')
              CALL                     2
              POP_TOP

250           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               11 (start_game + NULL|self)
              CALL                     0
              POP_TOP
              LOAD_CONST               5 (None)
              RETURN_VALUE

252   L3:     LOAD_GLOBAL              6 (messagebox)
              LOAD_ATTR               12 (showerror)
              PUSH_NULL
              LOAD_CONST               3 ('Error')
              LOAD_CONST               4 ('The order is incorrect. Please fix it or try again.')
              CALL                     2
              POP_TOP
              LOAD_CONST               5 (None)
              RETURN_VALUE

Disassembly of <code object start_training at 0x7f9a84343210, file "training.py", line 254>:
254           RESUME                   0

257           LOAD_FAST_BORROW         0 (root)
              LOAD_ATTR                1 (winfo_children + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER                19 (to L2)
              STORE_FAST               1 (widget)

258           LOAD_FAST_BORROW         1 (widget)
              LOAD_ATTR                3 (destroy + NULL|self)
              CALL                     0
              POP_TOP
              JUMP_BACKWARD           21 (to L1)

257   L2:     END_FOR
              POP_ITER

260           LOAD_GLOBAL              5 (TacoGame + NULL)
              LOAD_FAST_BORROW         0 (root)
              CALL                     1
              STORE_FAST               2 (app)

262           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (app, root)
              STORE_ATTR               3 (taco_game_app)
              LOAD_CONST               1 (None)
              RETURN_VALUE
