
let read_data () = 
  if (Array.length (Sys.argv))=1 then failwith "Utiisation : day11.exe <filename>";
  let filename = Sys.argv.(1) in
  let reader = open_in filename in
  let data = List.map int_of_string (String.split_on_char ' ' (input_line reader)) in
  data;;

let split n =
  let sn = string_of_int n in
  let l = String.length sn in
  (int_of_string (String.sub sn 0 (l/2)), int_of_string (String.sub sn (l/2) (l/2)));;

  let view_list l =
    List.iter (fun n -> Printf.printf "%d; " n) l; 
    print_newline ();;

let rec evolve l = 
  match l with
  | [] -> []
  | h::t when h=0 -> 1::(evolve t)
  | h::t when String.length (string_of_int h) mod 2 = 0 -> let n1, n2 = split h in n1::n2::(evolve t)
  | h::t -> (h*2024)::(evolve t);;



let () =
  let data = ref (read_data()) in
  for i = 1 to 25 do
    data := evolve !data;
  done;
  Printf.printf "Partie 1 = %d \n" (List.length !data)
  ;;

  
  