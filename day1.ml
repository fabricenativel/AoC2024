let rec read_data reader = 
  try
    let l = input_line reader in
    let fb = String.index l ' ' in
    let lb = String.rindex l ' ' in
    let n1 = int_of_string (String.sub l 0  fb) in
    let n2 = int_of_string (String.sub l (lb+1) (String.length l - lb - 1)) in
    let l1,l2 = read_data reader in
    n1::l1, n2::l2
  with
    End_of_file -> [],[]
    

let rec sum_diff l1 l2 =
  match l1,l2 with
  | [], _ -> 0
  | _, [] -> 0
  | h1::t1, h2::t2 -> abs(h1-h2) + sum_diff t1 t2;;

  
let () = let reader = open_in "day1.txt" in
        let l1, l2 = read_data reader in
        let lt1 = List.sort (fun a b -> a-b) l1  in
        let lt2 = List.sort (fun a b -> a-b) l2  in
        let res = sum_diff lt1 lt2 in
        Printf.printf "Résultat partie 1 = %d\n" res;;


