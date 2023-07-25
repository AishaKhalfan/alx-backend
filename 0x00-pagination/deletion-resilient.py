import json


def paginate_dataset(dataset, page, page_size):
    """Paginate a dataset in a deletion-resilient manner.

    Args:
        dataset: The dataset to paginate.
        page: The current page number.
        page_size: The number of items per page.

    Returns:
        A dictionary containing the paginated dataset and hypermedia metadata.
    """

    tombstones = []

    for item in dataset:
        if item['deleted']:
            tombstones.append(item['id'])

    paginated_dataset = [
        item for item in dataset if item['id'] not in tombstones
    ][(page - 1) * page_size:page * page_size]

    metadata = {
        "page": page,
        "page_size": page_size,
        "total_pages": len(dataset) - len(tombstones) // page_size + 1,
    }

    if page > 1:
        metadata["previous_page"] = page - 1

    if page < metadata["total_pages"]:
        metadata["next_page"] = page + 1

    return {"data": paginated_dataset, "meta": metadata}


def main():
    dataset = [
        {'id': 1, 'deleted': True},
        {'id': 2, 'deleted': True},
        {'id': 3, 'deleted': True},
        {'id': 4, 'deleted': True},
        {'id': 5, 'deleted': False},
    ]

    paginated_dataset = paginate_dataset(dataset, 1, 2)

    print(json.dumps(paginated_dataset, indent=2))


if __name__ == "__main__":
    main()
