<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove table rows for files that weren't created.
-->

Thư mục này giữ những thông tin cốt lõi về {Name}. Các ghi chú ở đây là nguồn chuẩn cho mọi việc khác.

## Các tệp

| Tệp | Dùng để | Thẻ nhóm |
|---|---|---|
| `me.md` | {Name} là ai, làm việc ra sao, muốn trợ lý AI làm việc thế nào | `identity` |
| `biography.md` | Câu chuyện của {Name} | `identity` |
| `goals.md` | Mục tiêu và ưu tiên | `goals` |
| `business.md` | Việc kinh doanh | `business` |
| `services.md` | Dịch vụ, sản phẩm, gói ưu đãi | `business` |
| `customers.md` | Ai mua và họ tìm đến {Name} bằng cách nào | `customers` |
| `pain-points.md` | Những vấn đề cần giải quyết | `customers` (hoặc `goals` nếu {Name} không bán gì) |
| `brand.md` | Giọng văn, cách nói, từ nên dùng và nên tránh | `brand` |
| `tools.md` | Công cụ và mỗi loại thông tin để ở đâu | `tools` |
| `cv.md` | Quá trình làm việc, học vấn, báo chí, giải thưởng | `career` |

## Khối thông tin (frontmatter)

Mọi tệp ở đây (trừ tệp này) đều bắt đầu bằng:

```yaml
---
type: about
status: active
updated: 2026-10-13
tags: [about, identity, working-style]
description: "{Name} là ai và muốn trợ lý AI làm việc thế nào."
---
```

- `type`: luôn là `about`.
- `status`: `active`, hoặc `outdated` khi biết chắc một thông tin đã cũ.
- `updated`: ngày thông tin thay đổi lần gần nhất. Không đổi khi chỉ sửa lỗi chính tả hay câu chữ.
- `tags`: `about`, rồi thẻ nhóm của tệp trong bảng trên, rồi các thẻ chủ đề nói tệp viết về gì (tiếng Anh, chữ thường, nối bằng gạch nối). Cập nhật thẻ chủ đề khi thêm hoặc bỏ một phần.
- `description`: một câu, trong dấu ngoặc kép, nói tệp này chứa gì. Luôn là dòng cuối.

## Quy tắc

- Các tệp này là nguồn chuẩn. Đừng chép nội dung của chúng sang chỗ khác: hãy liên kết tới chúng.
- Định dạng "hiện trạng ở trên, căn cứ ở dưới" (quy tắc gốc 17): tình hình hiện tại ở trên cùng, các căn cứ có ghi ngày ở bên dưới.
- Ngày sinh đầy đủ của {Name} chỉ nằm trong `me.md`. Không bao giờ chép hay nhắc lại nó trong câu trả lời. Năm sinh thì được.
- Chỉ tạo tệp mới khi có một chủ đề mới cần đến nó. Hỏi trước (quy tắc gốc 9).
- Khi kiểm tra tổng thể, đánh dấu những mục tiêu trong `goals.md` chưa có dự án nào đang chạy.
