import pandas as pd
from virtual_columns import add_virtual_column


def main():

    fruits_sales = pd.DataFrame({
        "name": ["banana", "apple", "orange", "mango"],
        "quantity": [10, 3, 5, 8],
        "price": [10, 1, 4, 6]
    })

    print("Original dataframe:")
    print(fruits_sales)

    result = add_virtual_column(fruits_sales, "quantity * price", "total")

    print("\nResult dataframe:")
    print(result)


if __name__ == "__main__":
    main()