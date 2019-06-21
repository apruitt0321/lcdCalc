use std::env;

fn lcd(nums: &Vec<i32>, x: i32) -> i32 {
    let v: Vec<bool> = nums.iter()
        .map(|y| {
            if x % y == 0 { 
                true
            } else {
                false 
            }
        }).collect();
    if v.contains(&false) {
        lcd(nums, x+1)
    } else {
        x
    }
}

fn main() {
    let args: Vec<i32> = env::args().skip(1)
        .map(|arg| {
            arg.parse::<i32>().unwrap()
        }).collect();
    let x = lcd(&args, 1);
    println!("The LCM of {:?} is {}", &args, &x);
}
