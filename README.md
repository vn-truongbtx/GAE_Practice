* Sign In / Sign Out
```
 GET /api/auth
```
- Resource:
```
  url:string
  url_linktext:string
  user_email:string
```
----------------------------------------------

* csrfToken
```
 GET /api/token
```
- Resource:
```
  csrftoken:string
```
----------------------------------------------

* Get List
```
 GET /api/messages/{guestbook_name}
```
- Resource:
```
  guestbook_name:string
  total_items: number
  next_cursor:next_cursor
  greetings:[
     id: string
     content: string
     date: string
     url: string
     author:string
     updated_by:string
     updated_date:string
 ]
```
----------------------------------------------

* Search List
```
 GET /api/messages/{guestbook_name}/search?content=
```
- Resource:
```
  guestbook_name:string
  total_items: number
  greetings:[
     id: string
     content: string
     date: string
     url: string
     author:string
     updated_by:string
     updated_date:string
 ]
 ```
----------------------------------------------

* Create
```
 POST /api/messages
```
- Request payload:
```
  guestbook_name: string
  content: string
```
----------------------------------------------

* Get Detail
```
 GET /api/messages/{guestbook_name}/{greeting_id}
```
- Resource:
```
   id: string
   content: string
   date: string
   url: string
   author:string
   updated_by:string
   updated_date:string
```
----------------------------------------------

* Delete
```
 DELETE /api/messages/{guestbook_name}/{greeting_id}
```
----------------------------------------------

* Update
```
 PUT /api/messages/{guestbook_name}/{greeting_id}
```
- Request payload:
```
  content: string
 ```