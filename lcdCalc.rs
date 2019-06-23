use std::env;
use std::io;

fn gcf(x: u32, y: u32) -> u32 {
    if y == 0 { x } 
    else { gcf(y, x % y) }
}

fn lcd(nums: &mut Vec<u32>) -> u32 {
    while nums.len() > 1 {
        let x = nums.pop().unwrap();
        let y = nums.pop().unwrap();
        nums.push((x*y) / gcf(x,y));
    }
    nums[0]
    //let a = nums.iter().fold(1, |acc, x| acc * *x);
    //a / nums.iter().fold(nums[0], |acc, x| gcf(acc, *x))
}

fn main() -> io::Result<()>{
    let args: Vec<u32> = env::args().skip(1)
        .map(|arg| {
            arg.parse::<u32>().unwrap()
        }).collect();
    let y = lcd(&mut args.clone());
    println!("The LCM of {:?} is {}", &args, y);
    Ok(())
}
