books = [
    (1, "Python Programming", "Guido", "CSE", 2, 500),
    (2, "Digital Logic", "Morris", "ECE", 2, 450),
    (3, "Thermodynamics", "Cengel", "MECH", 1, 600)
]

issued_books = []

issued_copies = {
    1: set(),
    2: set(),
    3: set()
}

waiting_list = {
    1: [],
    2: [],
    3: []
}

user_type_fine = {"student": 2, "faculty": 5}

issue_id = 100
wait_no = 1

while True:
    print("\n1.Issue Book")
    print("2.Return Book")
    print("3.Book Report")
    print("4.Search by Issue ID")
    print("5.Search by Book ID")
    print("6.Total Revenue & Utilization")
    print("7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        name = input("Name: ")
        roll = input("Roll No / Emp ID: ")
        user_type = input("User Type (student/faculty): ")
        issue_date = input("Issue Date: ")
        return_date = input("Return Date: ")

        total_copies = 0
        for b in books:
            if b[0] == book_id:
                total_copies = b[4]

        if book_id not in issued_copies:
            print("Invalid Book ID")
            continue

        if len(issued_copies[book_id]) < total_copies:
            copy_no = min(set(range(1, total_copies + 1)) - issued_copies[book_id])
            issued_copies[book_id].add(copy_no)
            issue_id += 1

            issued_books.append({
                "issue_id": issue_id,
                "book_id": book_id,
                "student_name": name,
                "roll_no": roll,
                "issue_date": issue_date,
                "return_date": return_date,
                "copy_no": copy_no,
                "fine_paid": 0,
                "user_type": user_type
            })

            print("Issued. Issue ID =", issue_id, "Copy No =", copy_no)

        else:
            waiting_list[book_id].append({
                "wait_no": wait_no,
                "name": name,
                "roll": roll,
                "user_type": user_type
            })
            print("Waiting List No =", wait_no)
            wait_no += 1

    elif choice == 2:
        ret_id = int(input("Enter Issue ID: "))
        days = int(input("Late Days: "))
        found = False

        for r in issued_books:
            if r["issue_id"] == ret_id:
                found = True
                book_id = r["book_id"]
                copy_no = r["copy_no"]
                user_type = r["user_type"]

                fine = days * user_type_fine[user_type]
                r["fine_paid"] = fine

                issued_books.remove(r)
                issued_copies[book_id].remove(copy_no)

                print("Returned. Fine =", fine)

                if waiting_list[book_id]:
                    w = waiting_list[book_id].pop(0)
                    issue_id += 1
                    issued_copies[book_id].add(copy_no)

                    issued_books.append({
                        "issue_id": issue_id,
                        "book_id": book_id,
                        "student_name": w["name"],
                        "roll_no": w["roll"],
                        "issue_date": "Auto",
                        "return_date": "Auto",
                        "copy_no": copy_no,
                        "fine_paid": 0,
                        "user_type": w["user_type"]
                    })

                    print("Auto Issued to", w["name"], "New Issue ID =", issue_id)
                break

        if not found:
            print("Issue ID Not Found")

    elif choice == 3:
        for b in books:
            book_id = b[0]
            total = b[4]
            issued = len(issued_copies[book_id])
            wait = len(waiting_list[book_id])
            revenue = 0

            for r in issued_books:
                if r["book_id"] == book_id:
                    revenue += r["fine_paid"]

            print(book_id, total, issued, wait, revenue)

    elif choice == 4:
        sid = int(input("Enter Issue ID: "))
        found = False
        for r in issued_books:
            if r["issue_id"] == sid:
                print(r)
                found = True
        if not found:
            print("Not Found")

    elif choice == 5:
        bid = int(input("Enter Book ID: "))
        found = False
        for r in issued_books:
            if r["book_id"] == bid:
                print(r["student_name"], r["roll_no"], r["copy_no"])
                found = True
        if not found:
            print("No Records")

    elif choice == 6:
        total_fine = 0
        total_copies = 0
        total_issued = 0

        for b in books:
            total_copies += b[4]
            total_issued += len(issued_copies[b[0]])

        for r in issued_books:
            total_fine += r["fine_paid"]

        if total_copies > 0:
            utilization = (total_issued / total_copies) * 100
        else:
            utilization = 0

        print("Total Revenue =", total_fine)
        print("Utilization % =", utilization)

    elif choice == 7:
        break

    else:
        print("Invalid Choice")