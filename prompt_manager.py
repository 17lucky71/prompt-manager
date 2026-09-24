# 프롬프트 관리 프로그램

# 이전 미션에서 작성한 프롬프트를 기본 데이터로 등록 (리스트 + 딕셔너리 구조)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 배경은 깔끔한 흰색 스튜디오 느낌으로, 제품이 돋보이도록 조명을 강조해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "이메일 초안 작성 도우미",
        "content": "당신은 정중하고 명확한 비즈니스 이메일을 작성하는 어시스턴트입니다. 아래 상황에 맞는 정중한 이메일 초안을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
]

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("제목은 비어있을 수 없습니다. 다시 입력해주세요.")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("내용은 비어있을 수 없습니다. 다시 입력해주세요.")

    print("\n카테고리 선택:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}) {cat}")
    print("(번호를 선택하거나, 목록에 없으면 직접 입력하세요)")

    cat_input = input("선택: ").strip()
    if cat_input.isdigit() and 1 <= int(cat_input) <= len(CATEGORIES):
        category = CATEGORIES[int(cat_input) - 1]
    elif cat_input:
        category = cat_input
    else:
        category = "기타"

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })

    print(f"\n'{title}' 프롬프트가 추가되었습니다!")


def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")

    print(f"\n총 {len(prompts)}개의 프롬프트")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            print("(카테고리별 조회 기능은 곧 추가됩니다)")
        elif choice == "4":
            print("(프롬프트 검색 기능은 곧 추가됩니다)")
        elif choice == "5":
            print("(프롬프트 상세 보기 기능은 곧 추가됩니다)")
        elif choice == "6":
            print("(즐겨찾기 관리 기능은 곧 추가됩니다)")
        elif choice == "7":
            print("(즐겨찾기 목록 기능은 곧 추가됩니다)")
        else:
            print("잘못된 번호입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()