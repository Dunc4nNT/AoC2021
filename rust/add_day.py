import sys
import pathlib

RUST_TEMPLATE = """fn process_data(input: &str) -> usize {

}

fn part1(input: &str) -> usize {

}


// fn part2(input: &str) -> usize {
// 
// }

fn main() {
    let input: &str = include_str!("input.txt");

    println!("Day {{day}}, Part 1: {:?}", part1(input));
    // println!("Day {{day}}, Part 2: {:?}", part2(input));
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
