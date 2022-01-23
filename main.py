import random as rng
import argparse as ap
import json
import yaml


def main(args):
    data = json.loads(open(args.input).read())

    if args.count_permutations:
        count_permutations(args, data)
    elif args.exhaust_permutations:
        exhaust_permutations(args, data)
    elif args.random_name:
        gen_rand_name(args, data)
    else:
        gen_rand_name(args, data)


def product(args):
    pools = list(map(tuple, args))
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def exhaust_permutations(args, data):
    if args.json:
        print(json.dumps([''.join(itm) for itm in product(data['word'])]))
    else:
        extra = ""
        ending = ""
        if args.endless_sky_phrase:
            print("""phrase "all possible names\"""")
            print("    word")
            extra="        \""
            ending = "\""
        for itm in product(data['word']):
            if args.yaml:
                extra = "- "
            print(f"""{extra}{''.join(itm)}{ending}""")


def gen_rand_name(args, data):
    print("".join([rng.choice(ls) for ls in data["word"]]))


def count_permutations(args, data):
    prev = len(data["word"][0])

    if args.verbose:
        print(f"Phrase 1: contains {prev} names")

    for idx, word in enumerate(data["word"][1:]):
        length = len(word)

        if args.verbose:
            print(f"Phrase {idx+2}: contains {length} names")

        prev = length * prev

    print(f"Phrase list has {prev} possible permutations")


if __name__ == "__main__":
    par = ap.ArgumentParser()
    par.add_argument("input", help="Input file (JSON).")
    par.add_argument("-v", "--verbose", action="store_true", help="More output")
    par.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="Skip confirmation (should be used with -p)"
    )

    list_modes_group = par.add_argument_group("list modes")
    list_modes = list_modes_group.add_mutually_exclusive_group()
    list_modes.add_argument(
        "-c",
        "--enumerate",
        action="store_true",
        help="Count possible names in list",
    )
    list_modes.add_argument(
        "-p",
        "--all-possible",
        action="store_true",
        help="Exhaust the list (print all possible names)",
    )
    list_modes.add_argument(
        "-r",
        "--random-name",
        action="store_true",
        help="Generate a random name from the list."
    )


    formats_group = par.add_argument_group("formats")
    formats = formats_group.add_mutually_exclusive_group()
    formats.add_argument(
        "-J","--json",
        action="store_true",
        help="Output JSON (should be used with -p)"
    )
    formats.add_argument(
        "-Y","--yaml",
        action="store_true",
        help="Output YAML (should be used with -p)"
    )
    formats.add_argument(
        "--endless-sky-phrase",
        action="store_true",
        help="Output Endless Sky plugin code (should be used with -p)."
    )

    args = par.parse_args()

    main(args)
