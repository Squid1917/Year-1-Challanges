def bubble_sort(items): 

    # Initialise the variables 

    num_items = len(items) 

    passes = 1 

    # Repeat while the maximum numbers of passes has not been made 

    numberlolidk = 0

    while passes < num_items: 

        # Repeat for each pair of items 

        for current in range(num_items - 1): 

            numberlolidk += 1

            # Compare the item at the current position with the next item 

            if items[current] > items[current+1]: 

                # Swap the out-of-order items 

                temp = items[current] 

                items[current] = items[current+1] 

                items[current+1] = temp 

        # Increase the number of passes by 1 

        passes = passes + 1 

    print(passes)
    return items

print(bubble_sort(["Maya", "Dan", "Vivian", "Tobi", "Areeji"]))