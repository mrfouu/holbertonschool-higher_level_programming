Apprentissage for python

```mermaid
graph TD
    start[Start] --> main[main.c]
    main --> display_prompt[display_prompt (prompt.c)]
    main --> read_line[read_line (line_read.c)]
    read_line --> tokenize[tokenize (line_parse.c)]
    tokenize --> handle_builtin[handle_builtin (building_handle.c)]
    handle_builtin --> print_env[print_env (env_print.c)]
    handle_builtin --> end[End]
    handle_builtin --> execute[execute (exec.c)]
    execute --> find_path[find_path (path_find.c)]
    execute --> end
    display_prompt --> read_line
