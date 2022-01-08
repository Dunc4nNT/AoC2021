import sys
import pathlib

RUST_TEMPLATE = """use std::time::Instant;

fn process_data(input: &str) -> usize {

}

fn part1(input: &str) -> usize {

}


// fn part2(input: &str) -> usize {
// 
// }

fn main() {
    let input: &str = include_str!("input.txt");

    let time1 = Instant::now();
    let solution1 = part1(input);
    let elapsed1 = time1.elapsed();
    println!("Day {{day}} Part 1: {:?} ({:?})", solution1, elapsed1);
    // let time2 = Instant::now();
    // let solution2 = part2(input);
    // let elapsed2 = time2.elapsed();
    // println!("Day {{day}}, Part 2: {:?} ({:?})", solution2, elapsed2);
}
"""

SOLUTION_TEMPLATE = """PART 1: 
PART 2: """

def create_template(day):
    template = RUST_TEMPLATE.replace("{{day}}", day)
    return template

def create_day(day, template):
    day_dir = pathlib.Path(f"src/bin/day{int(day):02}")
    if day_dir.exists():
        return

    day_dir.mkdir(parents=True, exist_ok=True)

    pathlib.Path(day_dir/"input.txt").touch()
    pathlib.Path(day_dir/"test.txt").touch()

    with open(day_dir/"solution.txt", "w") as fp:
        fp.write(SOLUTION_TEMPLATE)

    with open(day_dir/"main.rs", "w") as fp:
        fp.write(template)


def main():
    day = sys.argv[1]
    template = create_template(day)
    create_day(day, template)


if __name__ == "__main__":
    main()
