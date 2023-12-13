txt = []

# 읽기 권한으로 파일 열기
# with open("plain.txt", "r", encoding="utf-8") as f_r:
with open("plain.txt", "r") as f_r:
    # 변수에 해당 파일의 영문자를 소문자로 저장
    data = f_r.read().lower()

    Alphabet = 'abcdefghijklmnopqrstuvwxyz'

    freq = [0] * 26
    freq_dict = {}
    

    '''
    # 알파벳 빈도수
    '''
    
    for ch in data:
        # txt = [[before1, after1],[before2, after2]] 형식으로 저장
        txt.append([ch,'-'])
        if ch in Alphabet:
            # idx값이 a일때 0, b일때1, ..., z일때 25가 됨
            # freq = [a빈도수, b빈도수, ..., z빈도수]
            idx = Alphabet.find(ch)
            freq[idx] += 1

    # freq 배열을 내림차순으로 정렬할 경우, 순서가 섞이면 어떤 문자인지 알 수 없음
    # 따라서, freq_dict에 사전 형식으로 저장, key는 알파벳, value는 freq 배열의 값을 가짐
    # freq_dict = {'a' : a빈도수, 'b' : b빈도수, ...}
    for i in range(0,26):
        freq_dict[Alphabet[i]] = freq[i]

    # freq_dict를 내림차순으로 정렬
    sorted_freq = sorted(freq_dict.items(), key = lambda item: item[1], reverse = True)
    print("빈도수 별 알파벳 정렬_내림차순")
    print(sorted_freq)
    print('---------------------------------------------------------------------------')
    print(data)

    # alphabet_replace = []
    # user = input("> ")