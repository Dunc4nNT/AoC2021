use std::{collections::{HashMap, hash_map}, time::Instant};
use regex::Regex;

fn process_data(input: &str) -> HashMap<String, Vec<String>> {
    let mut caves: HashMap<String, Vec<String>> = HashMap::new();
    let re = Regex::new(r"(\w+)-(\w+)").unwrap();
    for line in input.lines() {
        let captures = re.captures(line).unwrap();
        match caves.entry(captures[1].to_string()) {
            hash_map::Entry::Vacant(e) => { e.insert(vec![captures[2].to_string()]); },
            hash_map::Entry::Occupied(mut e) => { e.get_mut().push(captures[2].to_string()) },
        }
        match caves.entry(captures[2].to_string()) {
            hash_map::Entry::Vacant(e) => { e.insert(vec![captures[1].to_string()]); },
            hash_map::Entry::Occupied(mut e) => { e.get_mut().push(captures[1].to_string()) },
        }
    }
    return caves;
}

fn find_paths(caves: HashMap<String, Vec<String>>, start_node: String, mut path: Vec<String>, mut hit: bool) -> Vec<Vec<String>> {
    let mut paths: Vec<Vec<String>> = Vec::new();
    path.push(start_node.clone());

    if start_node == "end" {
        return vec![path];
    }

    for node in caves.get(&start_node).unwrap().to_vec() {
        if node == "start" {
            continue;
        }

        if node.bytes().all(|b| matches!(b, b'A'..=b'Z')) {
            let new_paths = find_paths(caves.clone(), node, path.clone(), hit);
            for new_path in new_paths {
                paths.push(new_path);
            }
        } else if path.contains(&node) && !hit {
            hit = true;
            let new_paths = find_paths(caves.clone(), node, path.clone(), hit);
            hit = false;
            for new_path in new_paths {
                paths.push(new_path);
            }
        } else if node == "end" || !path.contains(&node) {
            let new_paths = find_paths(caves.clone(), node, path.clone(), hit);
            for new_path in new_paths {
                paths.push(new_path);
            }
        }
    }

    return paths;
}

fn part1(input: &str) -> usize {
    let caves = process_data(input);
    let result = find_paths(caves, "start".to_string(), vec![], true);

    return result.len().try_into().unwrap();
}

fn part2(input: &str) -> i32 {
    let caves = process_data(input);
    let result = find_paths(caves, "start".to_string(), vec![], false);

    return result.len().try_into().unwrap();
}

fn main() {
    let input: &str = include_str!("input.txt");

    let time1 = Instant::now();
    let solution1 = part1(input);
    let elapsed1 = time1.elapsed();
    println!("Day 9, Part 1: {:?} ({:?})", solution1, elapsed1);
    let time2 = Instant::now();
    let solution2 = part2(input);
    let elapsed2 = time2.elapsed();
    println!("Day 9, Part 2: {:?} ({:?})", solution2, elapsed2);
}
