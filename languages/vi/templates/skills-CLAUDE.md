<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Ghi chú và sở thích cho các kỹ năng (skill) mà trợ lý AI dùng, cùng với Quản gia.

## Cấu trúc

```
Skills/{skill-name}/
  {skill-name}.md hoặc SKILL.md   skill này làm gì
  ghi-chú.md                      giọng văn và sở thích của {Name} cho skill này
  references/                     ví dụ và tài liệu dài hơn
```

## Đã cài

| Kỹ năng | Thư mục | Làm gì |
|---|---|---|
| Quản gia | `brain-keeper/` | Tự dọn dẹp mỗi ngày, và kiểm tra tổng thể khi {Name} yêu cầu |
| Bản tin sáng | `morning-brief/` | Một kế hoạch ngắn cho ngày hôm nay, khi được yêu cầu hoặc mỗi ngày làm việc |
| Nhập ghi chú | `import/` | Đưa ghi chú từ ứng dụng khác vào, theo một kế hoạch {Name} duyệt trước |
| Chuẩn bị họp | `meeting-prep/` | Một bản tóm tắt ngắn trước cuộc gọi, từ các ghi chú trong bộ não |
| Công cụ tư duy | `thinking/` | Phản biện một ý tưởng, tìm quy luật, tìm những ghi chú nói ngược nhau |
| Ứng dụng đã kết nối | `connected-apps/` | Bộ não đọc từ những ứng dụng nào, và quy tắc cho chúng |
| No AI Slop | `no-ai-slop/` | Kiểm tra câu chữ: sửa bài viết cho nghe như người thật viết, hoặc chỉ ra các kiểu viết giống AI (của Peter Yang, giấy phép MIT, giữ nguyên, không sửa) |

## Quy tắc

- Mỗi skill một thư mục, đặt tên bằng chữ thường nối gạch nối (kebab-case).
- Khi thêm một skill mới, thêm một dòng vào bảng trên.
- Một `SKILL.md` lấy từ người khác thì không bao giờ được sửa. Muốn điều chỉnh một skill, hãy thêm `notes.md` vào thư mục của nó.
- `brain-keeper/daily.md` được một tác vụ chạy theo lịch đọc. Chỉ sửa nó khi muốn đổi việc mà lần chạy hằng ngày làm, và giữ nó đơn giản: không liên kết, không callout.
