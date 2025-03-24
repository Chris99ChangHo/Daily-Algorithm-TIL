import os

README_PATH = "README.md"
BASE_DIR = "Baekjoon"  # 문제 폴더 기준

def get_problem_list():
    problem_list = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".py") or file.endswith(".cpp") or file.endswith(".java"):
                problem_list.append(file)
    
    problem_list.sort()
    return problem_list

def update_readme():
    problem_list = get_problem_list()

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write("# Daily Algorithm TIL 🚀\n\n")
        f.write("## 📌 Solved Problems\n\n")
        
        for problem in problem_list:
            f.write(f"- {problem}\n")

        f.write("\n✅ 자동으로 업데이트됨! (GitHub Actions 활용)\n")

if __name__ == "__main__":
    update_readme()
