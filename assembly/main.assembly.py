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

  3           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              3 (settings_menu)
              STORE_NAME               3 (settings_menu)

  4           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              4 (training)
              STORE_NAME               4 (training)

  7           LOAD_CONST               3 ('\n _______       _____ ____  ____  ______ _      _      \n|__   __|/\\   / ____/ __ \\|  _ \\|  ____| |    | |     \n   | |  /  \\ | |   | |  | | |_\\) | |__  | |    | |     \n   | | / /\\ \\| |   | |  | |  _ <|  __| | |    | |     \n   | |/ ____ \\ |___| |__| | |_\\) | |____| |____| |____ \n   |_/_/    \\_\\_____\\____/|____/|______|______|______|\n')
              STORE_NAME               5 (TACO_BELL_BANNER)

 16           LOAD_CONST               4 (<code object show_login_screen at 0x55b7ab97cfe0, file "main.py", line 16>)
              MAKE_FUNCTION
              STORE_NAME               6 (show_login_screen)

 53           LOAD_CONST               5 (<code object show_main_menu at 0x55b7ab9949d0, file "main.py", line 53>)
              MAKE_FUNCTION
              STORE_NAME               7 (show_main_menu)

 78           LOAD_CONST               6 (<code object start_training at 0x7f2161cd0be0, file "main.py", line 78>)
              MAKE_FUNCTION
              STORE_NAME               8 (start_training)

 82           LOAD_CONST               7 (<code object settings at 0x7f2161aedfb0, file "main.py", line 82>)
              MAKE_FUNCTION
              STORE_NAME               9 (settings)

 86           LOAD_NAME               10 (__name__)
              LOAD_CONST               8 ('__main__')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE      116 (to L1)
              NOT_TAKEN

 88           LOAD_NAME                1 (tk)
              LOAD_ATTR               22 (Tk)
              PUSH_NULL
              CALL                     0
              STORE_NAME              12 (root)

 89           LOAD_NAME               12 (root)
              LOAD_ATTR               27 (title + NULL|self)
              LOAD_CONST               9 ('Taco Bell Training Simulator')
              CALL                     1
              POP_TOP

 92           LOAD_NAME               12 (root)
              LOAD_ATTR               29 (attributes + NULL|self)
              LOAD_CONST              10 ('-fullscreen')
              LOAD_CONST              11 (True)
              CALL                     2
              POP_TOP

 95           LOAD_NAME               12 (root)
              LOAD_ATTR               31 (bind + NULL|self)
              LOAD_CONST              12 ('<Escape>')
              LOAD_CONST              13 (<code object <lambda> at 0x7f2161b7a430, file "main.py", line 95>)
              MAKE_FUNCTION
              CALL                     2
              POP_TOP

 96           LOAD_NAME               12 (root)
              LOAD_ATTR               31 (bind + NULL|self)
              LOAD_CONST              14 ('<F11>')
              LOAD_CONST              15 (<code object <lambda> at 0x7f2161a5ac20, file "main.py", line 96>)
              MAKE_FUNCTION
              CALL                     2
              POP_TOP

 99           LOAD_NAME                6 (show_login_screen)
              PUSH_NULL
              CALL                     0
              POP_TOP

102           LOAD_NAME               12 (root)
              LOAD_ATTR               33 (mainloop + NULL|self)
              CALL                     0
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE

 86   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object show_login_screen at 0x55b7ab97cfe0, file "main.py", line 16>:
  --           MAKE_CELL                5 (password_entry)
               MAKE_CELL                6 (username_entry)

  16           RESUME                   0

  18           LOAD_GLOBAL              0 (root)
               LOAD_ATTR                3 (winfo_children + NULL|self)
               CALL                     0
               GET_ITER
       L1:     FOR_ITER                19 (to L2)
               STORE_FAST               0 (widget)

  19           LOAD_FAST_BORROW         0 (widget)
               LOAD_ATTR                5 (destroy + NULL|self)
               CALL                     0
               POP_TOP
               JUMP_BACKWARD           21 (to L1)

  18   L2:     END_FOR
               POP_ITER

  22           LOAD_GLOBAL              6 (tk)
               LOAD_ATTR                8 (Frame)
               PUSH_NULL
               LOAD_GLOBAL              0 (root)
               CALL                     1
               STORE_FAST               1 (top_spacer)

  23           LOAD_FAST_BORROW         1 (top_spacer)
               LOAD_ATTR               11 (pack + NULL|self)
               LOAD_CONST               0 (True)
               LOAD_CONST               1 (('expand',))
               CALL_KW                  1
               POP_TOP

  25           LOAD_GLOBAL              6 (tk)
               LOAD_ATTR                8 (Frame)
               PUSH_NULL
               LOAD_GLOBAL              0 (root)
               LOAD_SMALL_INT           2
               LOAD_GLOBAL              6 (tk)
               LOAD_ATTR               12 (RAISED)
               LOAD_SMALL_INT          40
               LOAD_SMALL_INT          40
               LOAD_CONST               2 (('bd', 'relief', 'padx', 'pady'))
               CALL_KW                  5
               STORE_FAST               2 (login_frame)

  26           LOAD_FAST_BORROW         2 (login_frame)
               LOAD_ATTR               11 (pack + NULL|self)
               LOAD_CONST               3 (False)
               LOAD_CONST               1 (('expand',))
               CALL_KW                  1
               POP_TOP

  28           LOAD_GLOBAL              6 (tk)
               LOAD_ATTR                8 (Frame)
               PUSH_NULL
               LOAD_GLOBAL              0 (root)
               CALL                     1
               STORE_FAST               3 (bottom_spacer)

  29           LOAD_FAST_BORROW         3 (bottom_spacer)
               LOAD_ATTR               11 (pack + NULL|self)
               LOAD_CONST               0 (True)
               LOAD_CONST               1 (('expand',))
               CALL_KW                  1
               POP_TOP

  31           LOAD_GLOBAL              6 (tk)
               LOAD_ATTR               14 (Label)
               PUSH_NULL
               LOAD_FAST_BORROW         2 (login_frame)
               LOAD_CONST               4 ('Taco Bell Simulator Login')
               LOAD_CONST              19 (('Helvetica', 24))
               LOAD_CONST               5 (('text', 'font'))
               CALL_KW                  3
               LOAD_ATTR               11 (pack + NULL|self)
               LOAD_SMALL_INT          20
               LOAD_CONST               6 (('pady',))
               CALL_KW                  1
               POP_TOP

  33           LOAD_GLOBAL              6 (tk)
               LOAD_ATTR               14 (Label)
               PUSH_NULL
               LOAD_FAST_BORROW         2 (login_frame)
               LOAD_CONST               7 ('Username:')
               LOAD_CONST              20 (('Helvetica', 16))
               LOAD_CONST               5 (('text', 'font'))
               CALL_KW                  3
               LOAD_ATTR               11 (pack + NULL|self)
               LOAD_SMALL_INT           5
               LOAD_CONST               6 (('pady',))
               CALL_KW                  1
               POP_TOP

  34           LOAD_GLOBAL              6 (tk)
               LOAD_ATTR               16 (Entry)
               PUSH_NULL
               LOAD_FAST_BORROW         2 (login_frame)
               LOAD_CONST              20 (('Helvetica', 16))
               LOAD_CONST               8 (('font',))
               CALL_KW                  2
               STORE_DEREF              6 (username_entry)

  35           LOAD_DEREF               6 (username_entry)
               LOAD_ATTR               11 (pack + NULL|self)
               LOAD_SMALL_INT           5
               LOAD_CONST               6 (('pady',))
               CALL_KW                  1
               POP_TOP

  37           LOAD_GLOBAL              6 (tk)
               LOAD_ATTR               14 (Label)
               PUSH_NULL
               LOAD_FAST_BORROW         2 (login_frame)
               LOAD_CONST               9 ('Password:')
               LOAD_CONST              20 (('Helvetica', 16))
               LOAD_CONST               5 (('text', 'font'))
               CALL_KW                  3
               LOAD_ATTR               11 (pack + NULL|self)
               LOAD_SMALL_INT           5
               LOAD_CONST               6 (('pady',))
               CALL_KW                  1
               POP_TOP

  38           LOAD_GLOBAL              6 (tk)
               LOAD_ATTR               16 (Entry)
               PUSH_NULL
               LOAD_FAST_BORROW         2 (login_frame)
               LOAD_CONST              10 ('*')
               LOAD_CONST              20 (('Helvetica', 16))
               LOAD_CONST              11 (('show', 'font'))
               CALL_KW                  3
               STORE_DEREF              5 (password_entry)

  39           LOAD_DEREF               5 (password_entry)
               LOAD_ATTR               11 (pack + NULL|self)
               LOAD_SMALL_INT           5
               LOAD_CONST               6 (('pady',))
               CALL_KW                  1
               POP_TOP

  41           LOAD_FAST_BORROW         5 (password_entry)
               LOAD_FAST_BORROW         6 (username_entry)
               BUILD_TUPLE              2
               LOAD_CONST              12 (<code object attempt_login at 0x7f2161b63ab0, file "main.py", line 41>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               STORE_FAST               4 (attempt_login)

  47           LOAD_GLOBAL              6 (tk)
               LOAD_ATTR               18 (Button)
               PUSH_NULL
               LOAD_FAST_BORROW         2 (login_frame)
               LOAD_CONST              13 ('Login')
               LOAD_CONST              20 (('Helvetica', 16))
               LOAD_FAST_BORROW         4 (attempt_login)
               LOAD_SMALL_INT          15
               LOAD_CONST              14 (('text', 'font', 'command', 'width'))
               CALL_KW                  5
               LOAD_ATTR               11 (pack + NULL|self)
               LOAD_SMALL_INT          20
               LOAD_CONST               6 (('pady',))
               CALL_KW                  1
               POP_TOP

  50           LOAD_GLOBAL              6 (tk)
               LOAD_ATTR               18 (Button)
               PUSH_NULL
               LOAD_GLOBAL              0 (root)
               LOAD_CONST              15 ('Exit Simulator')
               LOAD_CONST              21 (('Helvetica', 12))
               LOAD_GLOBAL              0 (root)
               LOAD_ATTR                4 (destroy)
               LOAD_CONST              16 (('text', 'font', 'command'))
               CALL_KW                  4
               LOAD_ATTR               11 (pack + NULL|self)
               LOAD_GLOBAL              6 (tk)
               LOAD_ATTR               20 (BOTTOM)
               LOAD_SMALL_INT          20
               LOAD_CONST              17 (('side', 'pady'))
               CALL_KW                  2
               POP_TOP
               LOAD_CONST              18 (None)
               RETURN_VALUE

Disassembly of <code object attempt_login at 0x7f2161b63ab0, file "main.py", line 41>:
  --           COPY_FREE_VARS           2

  41           RESUME                   0

  42           LOAD_DEREF               1 (username_entry)
               LOAD_ATTR                1 (get + NULL|self)
               CALL                     0
               LOAD_CONST               0 ('admin')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       34 (to L1)
               NOT_TAKEN
               LOAD_DEREF               0 (password_entry)
               LOAD_ATTR                1 (get + NULL|self)
               CALL                     0
               LOAD_CONST               1 ('password')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       13 (to L1)
               NOT_TAKEN

  43           LOAD_GLOBAL              3 (show_main_menu + NULL)
               CALL                     0
               POP_TOP
               LOAD_CONST               4 (None)
               RETURN_VALUE

  45   L1:     LOAD_GLOBAL              4 (messagebox)
               LOAD_ATTR                6 (showerror)
               PUSH_NULL
               LOAD_CONST               2 ('Error')
               LOAD_CONST               3 ('Invalid username or password')
               CALL                     2
               POP_TOP
               LOAD_CONST               4 (None)
               RETURN_VALUE

Disassembly of <code object show_main_menu at 0x55b7ab9949d0, file "main.py", line 53>:
 53           RESUME                   0

 55           LOAD_GLOBAL              0 (root)
              LOAD_ATTR                3 (winfo_children + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER                19 (to L2)
              STORE_FAST               0 (widget)

 56           LOAD_FAST_BORROW         0 (widget)
              LOAD_ATTR                5 (destroy + NULL|self)
              CALL                     0
              POP_TOP
              JUMP_BACKWARD           21 (to L1)

 55   L2:     END_FOR
              POP_ITER

 59           LOAD_GLOBAL              6 (tk)
              LOAD_ATTR                8 (Frame)
              PUSH_NULL
              LOAD_GLOBAL              0 (root)
              CALL                     1
              STORE_FAST               1 (top_frame)

 60           LOAD_FAST_BORROW         1 (top_frame)
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_GLOBAL              6 (tk)
              LOAD_ATTR               12 (TOP)
              LOAD_GLOBAL              6 (tk)
              LOAD_ATTR               14 (BOTH)
              LOAD_CONST               0 (True)
              LOAD_CONST               1 (('side', 'fill', 'expand'))
              CALL_KW                  3
              POP_TOP

 63           LOAD_GLOBAL              6 (tk)
              LOAD_ATTR               16 (Label)
              PUSH_NULL
              LOAD_FAST_BORROW         1 (top_frame)
              LOAD_GLOBAL             18 (TACO_BELL_BANNER)
              LOAD_CONST              10 (('Courier', 18, 'bold'))
              LOAD_GLOBAL              6 (tk)
              LOAD_ATTR               20 (LEFT)
              LOAD_CONST               2 (('text', 'font', 'justify'))
              CALL_KW                  4
              STORE_FAST               2 (banner_label)

 64           LOAD_FAST_BORROW         2 (banner_label)
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_CONST               0 (True)
              LOAD_CONST               3 (('expand',))
              CALL_KW                  1
              POP_TOP

 67           LOAD_GLOBAL              6 (tk)
              LOAD_ATTR                8 (Frame)
              PUSH_NULL
              LOAD_GLOBAL              0 (root)
              CALL                     1
              STORE_FAST               3 (bottom_frame)

 68           LOAD_FAST_BORROW         3 (bottom_frame)
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_GLOBAL              6 (tk)
              LOAD_ATTR               22 (BOTTOM)
              LOAD_GLOBAL              6 (tk)
              LOAD_ATTR               14 (BOTH)
              LOAD_CONST               0 (True)
              LOAD_CONST               1 (('side', 'fill', 'expand'))
              CALL_KW                  3
              POP_TOP

 70           LOAD_GLOBAL              6 (tk)
              LOAD_ATTR                8 (Frame)
              PUSH_NULL
              LOAD_FAST_BORROW         3 (bottom_frame)
              CALL                     1
              STORE_FAST               4 (buttons_frame)

 71           LOAD_FAST_BORROW         4 (buttons_frame)
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_CONST               0 (True)
              LOAD_CONST               3 (('expand',))
              CALL_KW                  1
              POP_TOP

 73           LOAD_GLOBAL              6 (tk)
              LOAD_ATTR               24 (Button)
              PUSH_NULL
              LOAD_FAST_BORROW         4 (buttons_frame)
              LOAD_CONST               4 ('Start Training')
              LOAD_CONST              11 (('Helvetica', 18))
              LOAD_SMALL_INT          20
              LOAD_GLOBAL             26 (start_training)
              LOAD_CONST               5 (('text', 'font', 'width', 'command'))
              CALL_KW                  5
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_SMALL_INT          10
              LOAD_CONST               6 (('pady',))
              CALL_KW                  1
              POP_TOP

 74           LOAD_GLOBAL              6 (tk)
              LOAD_ATTR               24 (Button)
              PUSH_NULL
              LOAD_FAST_BORROW         4 (buttons_frame)
              LOAD_CONST               7 ('Settings')
              LOAD_CONST              11 (('Helvetica', 18))
              LOAD_SMALL_INT          20
              LOAD_GLOBAL             28 (settings)
              LOAD_CONST               5 (('text', 'font', 'width', 'command'))
              CALL_KW                  5
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_SMALL_INT          10
              LOAD_CONST               6 (('pady',))
              CALL_KW                  1
              POP_TOP

 75           LOAD_GLOBAL              6 (tk)
              LOAD_ATTR               24 (Button)
              PUSH_NULL
              LOAD_FAST_BORROW         4 (buttons_frame)
              LOAD_CONST               8 ('Exit')
              LOAD_CONST              11 (('Helvetica', 18))
              LOAD_SMALL_INT          20
              LOAD_GLOBAL              0 (root)
              LOAD_ATTR                4 (destroy)
              LOAD_CONST               5 (('text', 'font', 'width', 'command'))
              CALL_KW                  5
              LOAD_ATTR               11 (pack + NULL|self)
              LOAD_SMALL_INT          10
              LOAD_CONST               6 (('pady',))
              CALL_KW                  1
              POP_TOP
              LOAD_CONST               9 (None)
              RETURN_VALUE

Disassembly of <code object start_training at 0x7f2161cd0be0, file "main.py", line 78>:
 78           RESUME                   0

 79           LOAD_GLOBAL              0 (training)
              LOAD_ATTR                2 (start_training)
              PUSH_NULL
              LOAD_GLOBAL              4 (root)
              CALL                     1
              POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object settings at 0x7f2161aedfb0, file "main.py", line 82>:
 82           RESUME                   0

 83           LOAD_GLOBAL              0 (settings_menu)
              LOAD_ATTR                2 (show_settings_menu)
              PUSH_NULL
              LOAD_GLOBAL              4 (root)
              LOAD_GLOBAL              6 (show_main_menu)
              CALL                     2
              POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x7f2161b7a430, file "main.py", line 95>:
 95           RESUME                   0
              LOAD_GLOBAL              0 (root)
              LOAD_ATTR                3 (attributes + NULL|self)
              LOAD_CONST               0 ('-fullscreen')
              LOAD_CONST               1 (False)
              CALL                     2
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x7f2161a5ac20, file "main.py", line 96>:
 96           RESUME                   0
              LOAD_GLOBAL              0 (root)
              LOAD_ATTR                3 (attributes + NULL|self)
              LOAD_CONST               0 ('-fullscreen')
              LOAD_GLOBAL              0 (root)
              LOAD_ATTR                3 (attributes + NULL|self)
              LOAD_CONST               0 ('-fullscreen')
              CALL                     1
              TO_BOOL
              UNARY_NOT
              CALL                     2
              RETURN_VALUE
