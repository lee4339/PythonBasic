print("-" * 10, "타이핑 프로그램 시작", "-" * 10)

# 사용자 입력을 저장할 리스트
save_data_list = []

# while문을 사용하여 무한 반복
while True:

    # 메뉴를 출력
    print("(1 : 데이터 저장, 2 : 데이터 출력, 3 : 파일에 저장, 0 : 종료)")
    
    # 메뉴 입력받는 변수
    input_menu = input("메뉴를 선택하세요 : ")

    # 입력된 메뉴 번호에 따라서 다른 동작을 하도록 elif 문 사용
    # 사용자가 입력하는 데이터를 저장
    if input_menu == "1":
        print("\n데이터를 입력하세요 :", end=" ")
        input_data = input()
        save_data_list.append(input_data)
        print("\n데이터를 저장했습니다.\n\n")
    # 사용자가 입력한 데이터를 화면에 출력
    elif input_menu == "2":
        # 메모리에 저장된 데이터가 있으면 화면에 출력, 없으면 없다는 메시지 출력
        if len(save_data_list) > 0:
            for data in save_data_list:
                print(data)
        else:
            print("\n입력된 데이터가 없습니다.\n\n")
    # 메모리에 저장된 데이터를 파일에 저장
    elif input_menu == "3":
        # 메모리에 저장된 데이터가 있으면 파일에 저장, 없으면 없다는 메시지 출력
        if len(save_data_list) > 0:
            f = open("testfile1.txt", "w", encoding="UTF-8")
            f.writelines("\n".join(save_data_list))
            f.close()
            # 파일 저장 후 메모리에 저장된 내용을 모두 삭제
            save_data_list.clear()
            print()
        else:
            print("\n저장된 데이터가 없습니다.\n\n")
    # 프로그램 종료
    elif input_menu == "0":
        print("\n프로그램을 종료합니다.")
        break
    else:
        print("\n잘못 입력하셨습니다.\n\n")