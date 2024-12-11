let read_data () = 
  if (Array.length (Sys.argv))=1 then failwith "Utiisation : day11.exe <filename>";
  let filename = Sys.argv.(1) in
  let reader = open_in filename in
  let data = List.map int_of_string (String.split_on_char ' ' (input_line reader)) in
  data;;

let insert_in_ht v k ht =
  if (Hashtbl.mem ht v) then let old = Hashtbl.find ht v in Hashtbl.replace ht v (old+k) else Hashtbl.add ht v k;;

let split n =
  let sn = string_of_int n in
  let l = String.length sn in
  (int_of_string (String.sub sn 0 (l/2)), int_of_string (String.sub sn (l/2) (l/2)));;


let  evolve ht = 
  let nht = Hashtbl.create (Hashtbl.length ht *  2) in
  Hashtbl.iter (fun v k -> 
    match v with
    | 0 -> insert_in_ht 1 k nht
    | n when String.length (string_of_int n) mod 2 = 0 -> let n1, n2 = split n in insert_in_ht n1 k nht; insert_in_ht n2 k nht;
    | n -> insert_in_ht (2024*n) k nht
    ) ht;
    nht;;

let rec view ht =
  Hashtbl.iter (fun v k  -> Printf.printf "(%d,%d) \n" v k) ht;
  print_endline "-----\n"
;;

let get_length ht =
  let values = List.of_seq (Hashtbl.to_seq_values ht) in
  List.fold_left ( + ) 0 values;;

let () =
  let data = read_data() in
  let state = ref (Hashtbl.create (2*List.length data)) in
  List.iter (fun n -> insert_in_ht  n 1 !state) data;
  for i = 1 to 75 do
    state := evolve !state;
  done;
  Printf.printf "Résultat partie 2 = %d\n" (get_length !state);;
  ;;

  
   