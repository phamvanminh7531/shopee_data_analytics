from django.shortcuts import render
import pandas as pd

def data_for_chart_1(df, real_category_value):
    doanh_thu_value_list = []
    doanh_so_value_list = []
    for category in real_category_value:
        doanh_thu_value = 0
        doanh_so_value = 0
        for i in range(len(df["category"])):
            if df["category"][i] == category:
                doanh_so_value += df["historical_sold"][i]
                doanh_thu_value += doanh_so_value*df["price"][i]
        doanh_thu_value_list.append(doanh_thu_value)
        doanh_so_value_list.append(doanh_so_value)
    return doanh_so_value_list, doanh_thu_value_list

def data_for_chart_2(df, real_category_value):

    cmt_count_value_list = []
    one_star_rating_value_list = []
    two_star_rating_value_list = []
    three_star_rating_value_list = []
    four_star_rating_value_list = []
    five_star_rating_value_list = []
    
    for category in real_category_value:
        cmt_count_value = 0
        one_star_rating_value = 0
        two_star_rating_value = 0
        three_star_rating_value = 0
        four_star_rating_value = 0
        five_star_rating_value = 0
        for i in range(len(df["category"])):
            if df["category"][i] == category:
                cmt_count_value += df["cmt_count"][i]
                one_star_rating_value += df["one_star_rating"][i]
                two_star_rating_value += df["two_star_rating"][i]
                three_star_rating_value += df["three_star_rating"][i]
                four_star_rating_value += df["four_star_rating"][i]
                five_star_rating_value += df["five_star_rating"][i]
        cmt_count_value_list.append(cmt_count_value)
        one_star_rating_value_list.append(one_star_rating_value)
        two_star_rating_value_list.append(two_star_rating_value)
        three_star_rating_value_list.append(three_star_rating_value)
        four_star_rating_value_list.append(four_star_rating_value)
        five_star_rating_value_list.append(five_star_rating_value)
    return cmt_count_value_list, one_star_rating_value_list, two_star_rating_value_list, three_star_rating_value_list, four_star_rating_value_list, five_star_rating_value_list

def data_chart_3(df, location_list):
    location_historical_list = []
    historical_sold_raito = []
    result_list = []
    for location in location_list:
        count_value = 0
        for i in range(len(df["shop_location"])):
            if df["shop_location"][i] == location:
                count_value += df["historical_sold"][i]
        location_historical_list.append(count_value)
    
    diff_count = 0
    for i in range(len(df["shop_location"])):
        if df["shop_location"][i] !='TP. Hồ Chí Minh' and df["shop_location"][i] != 'Hà Nội' and df["shop_location"][i] != 'Nước ngoài':
            diff_count+=1

    location_historical_list.append(diff_count)

    
    for i in location_historical_list:
        historical_sold_raito.append(i/sum(location_historical_list)*100)

    historical_sold_raito[-1]+=100-sum(historical_sold_raito)

    
    return historical_sold_raito


# Create your views here.
def index(request):
    real_category_value = ['bach_hoa', 'balo_tui_vi_nam', 'cham_soc_thu_cung',
       'dien_thoai_va_phu_kien', 'dong_ho', 'do_choi',
       'giat_giu_cham_soc_nha_cua', 'giay_dep_nam', 'giay_dep_nu',
       'may_anh_va_may_quay_phim', 'may_tinh_laptop', 'me_va_be',
       'nha_cua_doi_song', 'nha_sach_online', 'phu_kien_trang_suc_nu',
       'sac_dep', 'suc_khoe', 'the_thao_du_lich', 'thiet_bi_dien_tu',
       'thiet_bi_gia_dung', 'thoi_trang_nam', 'thoi_trang_nu',
       'thoi_trang_tre_em', 'tui_vi_nu', 'voucher_dich_vu', 'xe']
    
    category_tag = ["Bách Hóa", "Túi Ví Nam", "Thú Cưng", "Điện Thoại", "Đồng Hồ", "Đồ Chơi",
    "Chăm Sóc Nhà Cửa", "Giày Dép Nam", "Giày Dép Nữ", "Máy Ảnh - Máy Quay", "Máy Tính",
    "Mẹ Và Bé", "Đời Sống", "Sách", "Trang Sức Nữ", "Sắc Đẹp", "Sức Khỏe", "Thể Thao Du Lịch",
    "Thiết Bị Điện Tử", "Thiết Bị Gia Dụng", "Thời Trang Nam", "Thời Trang Nữ", "Thời Trang Trẻ Em",
    "Túi Ví Nữ", "Dịch Vụ", "Xe"
        ]
    

    location_list = ['TP. Hồ Chí Minh', 'Hà Nội', 'Nước ngoài']

    df = pd.read_csv('dashboard/shopee_sell_item_v1.csv', encoding='utf-8')
    doanh_so_value_list, doanh_thu_value_list = data_for_chart_1(df, real_category_value)
    cmt_count_value_list, one_star_rating_value_list, two_star_rating_value_list, three_star_rating_value_list, four_star_rating_value_list, five_star_rating_value_list = data_for_chart_2(df, real_category_value)

    chart_3_data = data_chart_3(df, location_list)

    tp_HCM = chart_3_data[0]
    Hanoi = chart_3_data[1]
    nuoc_ngoai = chart_3_data[2]
    con_lai = chart_3_data[3]

    doanh_thu_result_text = "Danh mục có doanh thu cao nhất là "+str(category_tag[doanh_thu_value_list.index(max(doanh_thu_value_list))])
    doanh_so_result_text = "Danh mục có doanh số cao nhất là "+str(category_tag[doanh_so_value_list.index(max(doanh_so_value_list))])
    danh_gia_text_reslt = category_tag[five_star_rating_value_list.index(max(five_star_rating_value_list))]+" là danh mục có đánh giá tích cực!"

    context = {
        "doanh_so_list":doanh_so_value_list,
        "doanh_thu_list":doanh_thu_value_list,
        
        "cmt_count":cmt_count_value_list,
        "one_star":one_star_rating_value_list,
        "two_star":two_star_rating_value_list,
        "three_star":three_star_rating_value_list,
        "four_star":four_star_rating_value_list,
        "five_star":five_star_rating_value_list,

        "tp_HCM":tp_HCM,
        "hanoi":Hanoi,
        "nuoc_ngoai":nuoc_ngoai,
        "con_lai":con_lai,

        "doanh_thu_result_text":doanh_thu_result_text,
        "doanh_so_result_text":doanh_so_result_text,
        "danh_gia_text_reslt":danh_gia_text_reslt,
    }

    return render(request, 'dashboard/index.html', context)