use std::env;

fn lcd(nums: &Vec<i32>, x: i32) -> i32 {
    let v: Vec<bool> = nums.iter().map(|y| {
        if x % y == 0 { 
            true
        } else {
            false
        }}).collect();
    if v.contains(&false) {
        lcd(nums, x+1)
    } else {
        x
    }
}

fn main() {
    let a: Vec<String> = env::args().collect();
    let args: Vec<i32> = a[1..].iter()
        .map(|y| {
            y.parse::<i32>().unwrap()
        }).collect();
    println!("{:?}", args);
    let x = lcd(&args, 1);
    println!("The LCM of {:?} is {}", &args, &x);
}
