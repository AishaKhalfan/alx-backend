import json


def paginate_dataset(dataset, page, page_size):
    """Paginate a dataset with hypermedia metadata.

    Args:
        dataset: The dataset to paginate.
        page: The current page number.
        page_size: The number of items per page.

    Returns:
        A dictionary containing the paginated dataset and hypermedia metadata.
    """

    paginated_dataset = dataset[(page - 1) * page_size:page * page_size]

    metadata = {
        "page": page,
        "page_size": page_size,
        "total_pages": len(dataset) // page_size + 1,
    }

    if page > 1:
        metadata["previous_page"] = page - 1

    if page < metadata["total_pages"]:
        metadata["next_page"] = page + 1

    return {"data": paginated_dataset, "meta": metadata}


def main():
    dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    paginated_dataset = paginate_dataset(dataset, 2, 3)

    print(json.dumps(paginated_dataset, indent=2))


if __name__ == "__main__":
    main()
