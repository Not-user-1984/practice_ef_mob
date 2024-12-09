data = [
    (1, "banana"),
    (2, "apple"),
    (3, "orange"),
]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
event_numbers = list(filter(lambda x: x * 2, numbers))


if __name__ == "__main__":
    print(sorted(data, key=lambda x: x[0]))
