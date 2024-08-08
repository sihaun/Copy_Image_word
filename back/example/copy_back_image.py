import os
import shutil

def copy_and_rename_image(image_path, count):
    # 파일명과 확장자 분리
    file_name, file_extension = os.path.splitext(image_path)

    # 이미지 파일이 존재하는지 확인
    if not os.path.exists(image_path):
        print(f"파일이 존재하지 않습니다: {image_path}")
        return

    # 숫자 규칙에 따라 파일 복사 및 이름 지정
    for i in range(count):
        # 네이밍 규칙 생성
        new_name = f"0{int(i/10)*10 + 10}.1{i}"

        # 새 파일 경로 생성
        new_file_path = f"{new_name}{file_extension}"
        
        # 파일 복사
        shutil.copy(image_path, new_file_path)
        print(f"파일 복사 완료: {new_file_path}")

# 예시 사용
image_path = "example.png"  # 원본 이미지 경로
count = 22  # 복사할 이미지 수
copy_and_rename_image(image_path, count)
