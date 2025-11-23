import json
import os

TASKS_FILE = "tasks.json"

tasks = []


def save_tasks():
	try:
		with open(TASKS_FILE, "w", encoding="utf-8") as f:
			json.dump(tasks, f, ensure_ascii=False, indent=2)
	except Exception as e:
		print(f"ไม่สามารถบันทึกไฟล์: {e}")


def load_tasks():
	global tasks
	if os.path.exists(TASKS_FILE):
		try:
			with open(TASKS_FILE, "r", encoding="utf-8") as f:
				data = json.load(f)
			if isinstance(data, list):
				tasks = data
			else:
				tasks = []
		except Exception as e:
			print(f"ไม่สามารถโหลดไฟล์: {e}")
			tasks = []
	else:
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
	if not tasks:
		print("ยังไม่มีงานในรายการ")
		return
	print(f"{'No.':<4} {'Title':<30} {'Due Date':<12} {'Status':<10}")
	for idx, t in enumerate(tasks, start=1):
		status = "เสร็จแล้ว" if t.get("completed") else "ยังไม่เสร็จ"
		title = t.get("title", "")[:30]
		due = t.get("due_date", "") or "-"
		print(f"{idx:<4} {title:<30} {due:<12} {status:<10}")


def edit_task():
	if not tasks:
		print("ยังไม่มีงานในรายการ")
		return
	# แสดงรายการเพื่อให้ผู้ใช้เลือก index
	view_tasks()
	idx_str = input("ระบุหมายเลขงานที่จะเแก้ไข (index): ").strip()
	try:
		idx = int(idx_str)
	except ValueError:
		print("ดัชนีไม่ถูกต้อง")
		return
	if idx < 1 or idx > len(tasks):
		print("ดัชนีไม่ถูกต้อง")
		return
	task = tasks[idx - 1]
	print(f"กำลังแก้ไขงาน id={task.get('id')}")
	new_title = input(f"ชื่อเรื่อง [{task.get('title')}]: ").strip()
	if new_title:
		task['title'] = new_title
	new_description = input(f"รายละเอียด [{task.get('description')}]: ").strip()
	if new_description:
		task['description'] = new_description
	# ให้ผู้ใช้เปลี่ยนสถานะ completed (y/n) หรือเว้นว่างเพื่อไม่เปลี่ยน
	current_status = 'y' if task.get('completed') else 'n'
	comp = input(f"สถานะเสร็จแล้ว? (y/n) [{current_status}]: ").strip().lower()
	if comp == 'y':
		task['completed'] = True
	elif comp == 'n':
		task['completed'] = False
	print("อัปเดตงานเรียบร้อย")


def delete_task():
	if not tasks:
		print("ยังไม่มีงานในรายการ")
		return
	# แสดงรายการเพื่อให้ผู้ใช้เลือก index
	view_tasks()
	idx_str = input("ระบุหมายเลขงานที่จะลบ (index): ").strip()
	try:
		idx = int(idx_str)
	except ValueError:
		print("ดัชนีไม่ถูกต้อง")
		return
	if idx < 1 or idx > len(tasks):
		print("ดัชนีไม่ถูกต้อง")
		return
	task = tasks[idx - 1]
	confirm = input(f"ต้องการลบงานนี้จริงหรือไม่ (y/n): ").strip().lower()
	if confirm == 'y':
		removed = tasks.pop(idx - 1)
		print(f"ลบงานเรียบร้อย (id={removed.get('id')}, title={removed.get('title')})")
	else:
		print("ยกเลิกการลบ")


def exit_program():
	save_tasks()
	print("บันทึกข้อมูลงานเรียบร้อย กำลังออกจากโปรแกรม...")


def main():
	load_tasks()
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