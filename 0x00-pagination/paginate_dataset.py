#!/usr/bin/env python3

def paginate_dataset(dataset, page, page_size):
    """Paginate a dataset.

    Args:
        dataset: The dataset to paginate.
        page: The current page number.
        page_size: The number of items per page.

    Returns:
        A list of items on the current page.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    paginated_dataset = dataset[start_index:end_index]

    return paginated_dataset


def main():
    dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    paginated_dataset = paginate_dataset(dataset, 4, 2)

    print(paginated_dataset)


if __name__ == "__main__":
    main()
