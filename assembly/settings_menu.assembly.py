  0           RESUME                   0

  1           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              0 (tkinter)
              STORE_NAME               1 (tk)

  2           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('messagebox',))
              IMPORT_NAME              0 (tkinter)
              IMPORT_FROM              2 (messagebox)
              STORE_NAME               2 (messagebox)
              POP_TOP

  4           LOAD_CONST               3 (<code object show_settings_menu at 0x55d2cadc5f70, file "settings_menu.py", line 4>)
              MAKE_FUNCTION
              STORE_NAME               3 (show_settings_menu)
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object show_settings_menu at 0x55d2cadc5f70, file "settings_menu.py", line 4>:
  --           MAKE_CELL                0 (root)
               MAKE_CELL               12 (fullscreen_var)

   4           RESUME                   0

   6           LOAD_DEREF               0 (root)
               LOAD_ATTR                1 (winfo_children + NULL|self)
               CALL                     0
               GET_ITER
       L1:     FOR_ITER                19 (to L2)
               STORE_FAST               2 (widget)

   7           LOAD_FAST_BORROW         2 (widget)
               LOAD_ATTR                3 (destroy + NULL|self)
               CALL                     0
               POP_TOP
               JUMP_BACKWARD           21 (to L1)

   6   L2:     END_FOR
               POP_ITER

  10           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR                6 (Label)
               PUSH_NULL
               LOAD_DEREF               0 (root)
               LOAD_CONST               0 ('Settings Menu')
               LOAD_CONST              40 (('Helvetica', 36, 'bold'))
               LOAD_CONST               1 (('text', 'font'))
               CALL_KW                  3
               LOAD_ATTR                9 (pack + NULL|self)
               LOAD_SMALL_INT          40
               LOAD_CONST               2 (('pady',))
               CALL_KW                  1
               POP_TOP

  13           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               10 (Frame)
               PUSH_NULL
               LOAD_DEREF               0 (root)
               CALL                     1
               STORE_FAST               3 (settings_frame)

  14           LOAD_FAST_BORROW         3 (settings_frame)
               LOAD_ATTR                9 (pack + NULL|self)
               LOAD_CONST               3 (True)
               LOAD_CONST               4 (('expand',))
               CALL_KW                  1
               POP_TOP

  17           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR                6 (Label)
               PUSH_NULL
               LOAD_FAST_BORROW         3 (settings_frame)
               LOAD_CONST               5 ('Audio Volume:')
               LOAD_CONST              41 (('Helvetica', 18))
               LOAD_CONST               1 (('text', 'font'))
               CALL_KW                  3
               LOAD_ATTR               13 (grid + NULL|self)
               LOAD_SMALL_INT           0
               LOAD_SMALL_INT           0
               LOAD_SMALL_INT          20
               LOAD_SMALL_INT          20
               LOAD_CONST               6 ('e')
               LOAD_CONST               7 (('row', 'column', 'padx', 'pady', 'sticky'))
               CALL_KW                  5
               POP_TOP

  18           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               14 (Scale)
               PUSH_NULL
               LOAD_FAST_BORROW         3 (settings_frame)
               LOAD_SMALL_INT           0
               LOAD_SMALL_INT         100
               LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               16 (HORIZONTAL)
               LOAD_CONST               8 (300)
               LOAD_CONST              42 (('Helvetica', 14))
               LOAD_CONST               9 (('from_', 'to', 'orient', 'length', 'font'))
               CALL_KW                  6
               STORE_FAST               4 (volume_scale)

  19           LOAD_FAST_BORROW         4 (volume_scale)
               LOAD_ATTR               19 (set + NULL|self)
               LOAD_SMALL_INT          75
               CALL                     1
               POP_TOP

  20           LOAD_FAST_BORROW         4 (volume_scale)
               LOAD_ATTR               13 (grid + NULL|self)
               LOAD_SMALL_INT           0
               LOAD_SMALL_INT           1
               LOAD_SMALL_INT          20
               LOAD_SMALL_INT          20
               LOAD_CONST              10 (('row', 'column', 'padx', 'pady'))
               CALL_KW                  4
               POP_TOP

  23           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR                6 (Label)
               PUSH_NULL
               LOAD_FAST_BORROW         3 (settings_frame)
               LOAD_CONST              11 ('Difficulty Level:')
               LOAD_CONST              41 (('Helvetica', 18))
               LOAD_CONST               1 (('text', 'font'))
               CALL_KW                  3
               LOAD_ATTR               13 (grid + NULL|self)
               LOAD_SMALL_INT           1
               LOAD_SMALL_INT           0
               LOAD_SMALL_INT          20
               LOAD_SMALL_INT          20
               LOAD_CONST               6 ('e')
               LOAD_CONST               7 (('row', 'column', 'padx', 'pady', 'sticky'))
               CALL_KW                  5
               POP_TOP

  24           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               20 (StringVar)
               PUSH_NULL
               LOAD_CONST              12 ('Normal')
               LOAD_CONST              13 (('value',))
               CALL_KW                  1
               STORE_FAST               5 (difficulty_var)

  25           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               22 (OptionMenu)
               PUSH_NULL
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 53 (settings_frame, difficulty_var)
               LOAD_CONST              14 ('Beginner')
               LOAD_CONST              15 ('Intermediate')
               LOAD_CONST              16 ('Hard')
               LOAD_CONST              17 ('Expert')
               CALL                     6
               STORE_FAST               6 (difficulty_menu)

  26           LOAD_FAST_BORROW         6 (difficulty_menu)
               LOAD_ATTR               25 (config + NULL|self)
               LOAD_CONST              42 (('Helvetica', 14))
               LOAD_SMALL_INT          18
               LOAD_CONST              18 (('font', 'width'))
               CALL_KW                  2
               POP_TOP

  27           LOAD_FAST_BORROW         6 (difficulty_menu)
               LOAD_ATTR               13 (grid + NULL|self)
               LOAD_SMALL_INT           1
               LOAD_SMALL_INT           1
               LOAD_SMALL_INT          20
               LOAD_SMALL_INT          20
               LOAD_CONST              19 ('w')
               LOAD_CONST               7 (('row', 'column', 'padx', 'pady', 'sticky'))
               CALL_KW                  5
               POP_TOP

  30           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR                6 (Label)
               PUSH_NULL
               LOAD_FAST_BORROW         3 (settings_frame)
               LOAD_CONST              20 ('Shift Duration:')
               LOAD_CONST              41 (('Helvetica', 18))
               LOAD_CONST               1 (('text', 'font'))
               CALL_KW                  3
               LOAD_ATTR               13 (grid + NULL|self)
               LOAD_SMALL_INT           2
               LOAD_SMALL_INT           0
               LOAD_SMALL_INT          20
               LOAD_SMALL_INT          20
               LOAD_CONST               6 ('e')
               LOAD_CONST               7 (('row', 'column', 'padx', 'pady', 'sticky'))
               CALL_KW                  5
               POP_TOP

  31           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               20 (StringVar)
               PUSH_NULL
               LOAD_CONST              21 ('8 Hours')
               LOAD_CONST              13 (('value',))
               CALL_KW                  1
               STORE_FAST               7 (shift_var)

  32           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               22 (OptionMenu)
               PUSH_NULL
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 55 (settings_frame, shift_var)
               LOAD_CONST              22 ('4 Hours')
               LOAD_CONST              23 ('6 Hours')
               LOAD_CONST              21 ('8 Hours')
               LOAD_CONST              24 ('12 Hours (Double Shift)')
               CALL                     6
               STORE_FAST               8 (shift_menu)

  33           LOAD_FAST_BORROW         8 (shift_menu)
               LOAD_ATTR               25 (config + NULL|self)
               LOAD_CONST              42 (('Helvetica', 14))
               LOAD_SMALL_INT          18
               LOAD_CONST              18 (('font', 'width'))
               CALL_KW                  2
               POP_TOP

  34           LOAD_FAST_BORROW         8 (shift_menu)
               LOAD_ATTR               13 (grid + NULL|self)
               LOAD_SMALL_INT           2
               LOAD_SMALL_INT           1
               LOAD_SMALL_INT          20
               LOAD_SMALL_INT          20
               LOAD_CONST              19 ('w')
               LOAD_CONST               7 (('row', 'column', 'padx', 'pady', 'sticky'))
               CALL_KW                  5
               POP_TOP

  37           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               26 (BooleanVar)
               PUSH_NULL
               LOAD_DEREF               0 (root)
               LOAD_ATTR               29 (attributes + NULL|self)
               LOAD_CONST              25 ('-fullscreen')
               CALL                     1
               LOAD_CONST              13 (('value',))
               CALL_KW                  1
               STORE_DEREF             12 (fullscreen_var)

  38           LOAD_FAST_BORROW        12 (fullscreen_var)
               LOAD_FAST_BORROW         0 (root)
               BUILD_TUPLE              2
               LOAD_CONST              26 (<code object toggle_fullscreen at 0x7fc5f70edfb0, file "settings_menu.py", line 38>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               STORE_FAST               9 (toggle_fullscreen)

  41           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               30 (Checkbutton)
               PUSH_NULL

  42           LOAD_FAST_BORROW         3 (settings_frame)

  43           LOAD_CONST              27 ('Fullscreen Mode')

  44           LOAD_DEREF              12 (fullscreen_var)

  45           LOAD_FAST_BORROW         9 (toggle_fullscreen)

  46           LOAD_CONST              41 (('Helvetica', 18))

  41           LOAD_CONST              28 (('text', 'variable', 'command', 'font'))
               CALL_KW                  5

  47           LOAD_ATTR               13 (grid + NULL|self)
               LOAD_SMALL_INT           3
               LOAD_SMALL_INT           0
               LOAD_SMALL_INT           2
               LOAD_SMALL_INT          30
               LOAD_CONST              29 (('row', 'column', 'columnspan', 'pady'))
               CALL_KW                  4
               POP_TOP

  50           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               10 (Frame)
               PUSH_NULL
               LOAD_DEREF               0 (root)
               CALL                     1
               STORE_FAST              10 (btn_frame)

  51           LOAD_FAST_BORROW        10 (btn_frame)
               LOAD_ATTR                9 (pack + NULL|self)
               LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               32 (BOTTOM)
               LOAD_SMALL_INT          50
               LOAD_CONST              30 (('side', 'pady'))
               CALL_KW                  2
               POP_TOP

  53           LOAD_CONST              31 (<code object saved_prompt at 0x7fc5f72d0be0, file "settings_menu.py", line 53>)
               MAKE_FUNCTION
               STORE_FAST              11 (saved_prompt)

  56           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               34 (Button)
               PUSH_NULL
               LOAD_FAST_BORROW        10 (btn_frame)
               LOAD_CONST              32 ('Apply Settings')
               LOAD_CONST              41 (('Helvetica', 18))
               LOAD_SMALL_INT          20
               LOAD_CONST              33 ('#4CAF50')
               LOAD_CONST              34 ('white')
               LOAD_FAST_BORROW        11 (saved_prompt)
               LOAD_CONST              35 (('text', 'font', 'width', 'bg', 'fg', 'command'))
               CALL_KW                  7
               LOAD_ATTR                9 (pack + NULL|self)
               LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               36 (LEFT)
               LOAD_SMALL_INT          10
               LOAD_CONST              36 (('side', 'padx'))
               CALL_KW                  2
               POP_TOP

  57           LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               34 (Button)
               PUSH_NULL
               LOAD_FAST_BORROW        10 (btn_frame)
               LOAD_CONST              37 ('Back to Main Menu')
               LOAD_CONST              41 (('Helvetica', 18))
               LOAD_SMALL_INT          20
               LOAD_FAST_BORROW         1 (on_back)
               LOAD_CONST              38 (('text', 'font', 'width', 'command'))
               CALL_KW                  5
               LOAD_ATTR                9 (pack + NULL|self)
               LOAD_GLOBAL              4 (tk)
               LOAD_ATTR               36 (LEFT)
               LOAD_SMALL_INT          10
               LOAD_CONST              36 (('side', 'padx'))
               CALL_KW                  2
               POP_TOP
               LOAD_CONST              39 (None)
               RETURN_VALUE

Disassembly of <code object toggle_fullscreen at 0x7fc5f70edfb0, file "settings_menu.py", line 38>:
  --           COPY_FREE_VARS           2

  38           RESUME                   0

  39           LOAD_DEREF               1 (root)
               LOAD_ATTR                1 (attributes + NULL|self)
               LOAD_CONST               0 ('-fullscreen')
               LOAD_DEREF               0 (fullscreen_var)
               LOAD_ATTR                3 (get + NULL|self)
               CALL                     0
               CALL                     2
               POP_TOP
               LOAD_CONST               1 (None)
               RETURN_VALUE

Disassembly of <code object saved_prompt at 0x7fc5f72d0be0, file "settings_menu.py", line 53>:
 53           RESUME                   0

 54           LOAD_GLOBAL              0 (messagebox)
              LOAD_ATTR                2 (showinfo)
              PUSH_NULL
              LOAD_CONST               0 ('Settings')
              LOAD_CONST               1 ('Settings applied successfully!')
              CALL                     2
              POP_TOP
              LOAD_CONST               2 (None)
              RETURN_VALUE
