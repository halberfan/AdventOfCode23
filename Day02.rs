use std::fs;

const DAY: &str = "02";

pub fn solve(input: bool) -> (i32, i32) {
    (solve_one(input), solve_two(input))
}

fn get_file(input: bool) -> String {
    let t = match input {
        true => "input.txt",
        false => "demo.txt",
    };
    fs::read_to_string(format!("src/input/day{DAY}/{t}")).expect("Should have been able to read the file")
}

fn solve_one(input: bool) -> i32 {
    let contents = get_file(input);

    let control: [i32; 3] = [12, 13, 14];

    let mut sum = 0;

    for line in contents.split("\n") {
        let game = line.split(":").collect::<Vec<_>>();
        let a: &str = game[1];
        let id = &game[0][5..game[0].len()];
        let id: i32 = id.parse().unwrap();
        let mut br: bool = false;
        for p in a.split(";") {
            if br { break; }
            for b in p.split(",") {
                let arg = b[1..b.len()].split(" ").collect::<Vec<_>>();
                let i = match arg[1].replace("\r", "").as_str() {
                    "green" => 1,
                    "blue" => 2,
                    "red" => 0,
                    _ => 99
                };
                let amount: i32 = arg[0].parse().unwrap();
                if amount > control[i] {
                    br = true;
                    break;
                }
            }
        }

        if !br { sum += id };
    }

    sum
}

fn solve_two(input: bool) -> i32 {
    let contents = get_file(input);

    let mut c: [i32; 3] = [0, 0, 0];

    let mut sum = 0;

    for line in contents.split("\n") {
        let game = line.split(":").collect::<Vec<_>>();
        let a: &str = game[1];
        for p in a.split(";") {
            for b in p.split(",") {
                let arg = b[1..b.len()].split(" ").collect::<Vec<_>>();
                let i = match arg[1].replace("\r", "").as_str() {
                    "green" => 1,
                    "blue" => 2,
                    "red" => 0,
                    _ => 99
                };
                let amount: i32 = arg[0].parse().unwrap();
                if c[i] < amount {
                    c[i] = amount;
                }
            }
        }

        sum += c[0] * c[1] * c[2];
        c[0] = 0; c[1] = 0; c[2] = 0;
    }

    sum
}
