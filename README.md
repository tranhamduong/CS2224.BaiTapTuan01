# CS2224.BaiTapTuan01


# How to run
1. Installation 
``
pip install -r requirements.txt
``

2. Run program: 
``
python3 console.py
``

3. Format input: 

``
TERM_1 AND TERM_2 AND TERM_3 ... AND NOT TERM_X AND TERM_Y ANDNOT TERM_Z (*)
``

Ví dụ: 
- TERM_1 AND TERM_2 => Truy vấn document có từ TERM_1 và từ TERM_2
- TERM_1 AND NOT TERM_2 =>  Truy vấn document có từ TERM_1 và không có từ TERM_2
- TERM_1 AND TERM_2 AND NOT TERM_3 =>  Truy vấn document có từ TERM_1 và TERM_2, không có từ TERM_3

``
tại AND Việt AND Nam
``

_Answer:_
```
Found terms in this document 18
Bán lẻ Nhật Bản đua mở rộng tại Việt Nam
```

``
tại AND NOT Việt AND NOT Nam
``

_Answer:_
```
Found terms in this document 95
Nhiều tỉnh cách ly F0 tại nhà
Found terms in this document 76
Người đẹp Hong Kong gây thích thú tại Miss Grand
Found terms in this document 153
Barca thắng trận sân khách đầu tiên tại La Liga
Found terms in this document 204
Thùy Tiên tự tin thể hiện tại Miss Grand
Found terms in this document 157
Giá căn hộ tại phố nhà giàu đua lập đỉnh
Found terms in this document 12
Trung Quốc muốn hãng gọi xe Didi rút niêm yết tại Mỹ
Found terms in this document 210
Hoà Phát 'xin thêm' hơn 1.600 ha làm các dự án tại Khu kinh tế Dung Quất
Found terms in this document 104
Hai máy bay va chạm tại sân đỗ Nội Bài
Found terms in this document 170
Juventus thua trận thứ năm tại Serie A
Found terms in this document 25
Doanh nghiệp tự chọn cách xét nghiệm Covid-19 tại nơi làm việc
Found terms in this document 35
Mỹ nhân đầu trọc tại Miss World 2021
Found terms in this document 28
Bốn giả thiết về Covid-19 suy yếu tại Nhật Bản
Found terms in this document 191
Cứu F0 nặng tại ICU lớn nhất miền Bắc
```

**(*) Chữ AND / AND NOT phải viết _in hoa_**

4. Nếu muốn dùng word_segmentation
- Trong config.py -> sửa title_file thành "vnexpress_271_titles_segmented.txt" (và ngược lại) 
- Lúc này, câu query phải được segmented sẵn --> Nếu không sẽ truy vấn không tốt (gần như thất bại)

VD: 
``
tại AND Việt_Nam
``

_Answer:_


```
Found terms in this document 18
Bán_lẻ Nhật_Bản_đua mở_rộng tại Việt_Nam
```

``
tại AND NOT Việt_Nam
``

_Answer:_ 

```
Found terms in this document 25
Doanh_nghiệp tự chọn cách xét_nghiệm Covid-19 tại nơi làm_việc
Found terms in this document 153
Barca thắng trận sân khách đầu_tiên tại La_Liga
Found terms in this document 204
Thùy Tiên tự_tin thể_hiện tại Miss_Grand
Found terms in this document 35
Mỹ_nhân đầu trọc tại Miss_World 2021
Found terms in this document 157
Giá căn_hộ tại phố nhà giàu đua lập đỉnh
Found terms in this document 147
Độ nguy_hiểm của siêu biến_chủng mới tại Nam_Phi
Found terms in this document 210
Hoà_Phát ' xin thêm ' hơn 1.600 ha làm các dự_án tại Khu kinh_tế Dung Quất
Found terms in this document 104
Hai máy_bay va_chạm tại sân đỗ Nội_Bài
Found terms in this document 28
Bốn giả_thiết về Covid-19 suy_yếu tại Nhật_Bản
Found terms in this document 95
Nhiều tỉnh cách_ly F0 tại nhà
Found terms in this document 191
Cứu F0 nặng tại ICU lớn nhất miền Bắc
Found terms in this document 76
Người đẹp Hong_Kong gây thích_thú tại Miss_Grand
Found terms in this document 170
Juventus thua trận thứ năm tại Serie_A
Found terms in this document 12
Trung_Quốc muốn hãng gọi xe Didi rút niêm_yết tại Mỹ
```


``
tại AND NOT Việt Nam
``

_Answer_
```
...

Found terms in this document 18 =========> Vì khi indexing thì indexing cụm Việt_Nam nên kết quả có từ "Việt Nam" vẫn xuất hiện
Bán_lẻ Nhật_Bản_đua mở_rộng tại Việt_Nam
...
```

5. Việc indexing được ghi ra file
- File Dictionary.txt 
- File Dictionary_segmented.txt

6. Data được crawl từ báo vnexpress.net => Chi tiết trong file ``vnexpress_crawler.py ``
7. Code indexing tham khảo từ [Nguồn](https://github.com/asadmohammad/Boolean-Retrieval-Model)
