tasks = []


def add_task():
	title = input("ชื่อเรื่อง: ").strip()
	description = input("รายละเอียด: ").strip()
	due_date = input("วันครบกำหนด (เช่น YYYY-MM-DD): ").strip()
	if tasks:
		new_id = max(t["id"] for t in tasks) + 1
	else:
		new_id = 1
	task = {
		"id": new_id,
		"title": title,
		"description": description,
		"due_date": due_date,
		"completed": False,
	}
	tasks.append(task)
	print(f"เพิ่มงานเรียบร้อย (id={new_id})")


def view_tasks():
	pass


def edit_task():
	pass


def delete_task():
	pass


def exit_program():
	pass


def main():
	while True:
		print("===== เมนู ToDo List =====")
		print("1. เพิ่มงานใหม่")
		print("2. ดูงานทั้งหมด")
		print("3. แก้ไขงาน")
		print("4. ลบงาน")
		print("5. ออกจากโปรแกรม")
		choice = input("เลือกเมนู (1-5): ").strip()
		if choice == "1":
			add_task()
		elif choice == "2":
			view_tasks()
		elif choice == "3":
			edit_task()
		elif choice == "4":
			delete_task()
		elif choice == "5":
			exit_program()
			break
		else:
			print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")


if __name__ == "__main__":
	main()