@startuml
class Task {
  + id: Integer
  + title: String
  + description: Text
  + status: Boolean
  + created_at: DateTime
}

class Views {
  + create_task()
  + list_tasks()
  + update_task()
  + delete_task()
}

class URLs {
  + /tasks/create
  + /tasks
  + /tasks/update/<id>
  + /tasks/delete/<id>
}

class Templates {
  + task_list.html
  + task_form.html
}

Task --> Views : Accessed by
Views --> URLs : Mapped to
URLs --> Templates : Rendered in
@enduml
