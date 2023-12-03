use std::fs;

const DAY: &str = "01";

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
    let mut sum = 0;
    for x in contents.split("\n") {
        let s: String = String::from(x);
        let mut found_first = false;
        let mut first = '0';
        let mut last = '0';
        for x in s.chars() {
            let n = match x {
                '0'..='9' => true,
                _ => false
            };
            if n {
                if !found_first {
                    first = x;
                    found_first = true;
                }
                last = x;
            }
        }

        let mut s = String::from(first);
        s.push(last);
        sum += s.trim().parse::<i32>().unwrap();
    }

    sum
}

fn solve_two(input: bool) -> i32 {
    let contents: String = get_file(input);
    let mut sum = 0;
    for x in contents.split("\n") {
        let mut s: String = String::from("");
        let mut found_first = false;
        let mut first = '0';
        let mut last = '0';
        for x in x.chars() {
            s.push(x);
            let n = match x {
                '0'..='9' => true,
                _ => { false }
            };
            if n {
                s.clear();
                if x != '-' {
                    if !found_first {
                        first = x;
                        found_first = true;
                    }
                    last = x;
                }
            } else {
                for i in 0..s.len() {
                    let s = &s[i..s.len()];
                    let x = if s.contains("one") {
                        '1'
                    } else if s.contains("two") {
                        '2'
                    } else if s.contains("three") {
                        '3'
                    } else if s.contains("four") {
                        '4'
                    } else if s.contains("five") {
                        '5'
                    } else if s.contains("six") {
                        '6'
                    } else if s.contains("seven") {
                        '7'
                    } else if s.contains("eight") {
                        '8'
                    } else if s.contains("nine") {
                        '9'
                    } else {
                        '-'
                    };
                    if x != '-' {
                        if !found_first {
                            first = x;
                            found_first = true;
                        }
                        last = x;
                    }
                }
            }
        }
        let mut s = String::from(first);
        s.push(last);
        sum += s.trim().parse::<i32>().unwrap();
    }
    sum
}
