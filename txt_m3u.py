def txt_to_m3u():
   

    # 打开m3u文件并写入内容
    with open('IPTV_Z.m3u', 'w', encoding='utf-8') as f:
        f.write('#EXTM3U\n')
        print(f"写入文件开始。")
        f.write(f'#EXTINF:-1 group-title="AAA","http://kuanglong.vicp.hk:2121/udp/239.93.16.118:8708"\n')
        # 初始化genre变量
        genre = ''

        # 遍历txt文件内容
        # for line in lines:
        #     line = line.strip()
        #     if line:
        #         # 检查是否是genre行
        #         channel_name, channel_url = line.split(',', 1)
        #         if channel_url == '#genre#':
        #             genre = channel_name
        #             print(genre)
        #         else:
        #             # 将频道信息写入m3u文件
        #             f.write(f'#EXTINF:-1 group-title="{genre}",{channel_name}\n')
        #             f.write(f'{channel_url}\n')
        print(f"写入文件结束。")

    #fr.close()
    f.close()

# 将txt文件转换为m3u文件
txt_to_m3u()

print(f"m3u文件创建成功,IPTV_Z.m3u")