import pandas as pd
sv = {
    "MSSV":    [2301, 2302, 2401],
    "HoTen":   ["Ly Thi Hong", "Nguyen Van Hai", "Le Phuong Anh"],
    "NamSinh": [2000, 2002, 2001],
    "DiaChi":  ["HCM", "VT", "DN"],
}
df = pd.DataFrame(sv)
df["GioiTinh"] = ["Nu", "Nam", "Nu"]
print(df)
df_them = pd.DataFrame({
    "MSSV":     [2306, 2404, 2304],
    "HoTen":    ["Nguyen Van Tai", "Le Van Nam", "Phan Hong Tham"],
    "NamSinh":  [2002, 2001, 2001],
    "DiaChi":   ["NT", "VT", "HCM"],
    "GioiTinh": ["Nam", "Nam", "Nu"],
})
df = pd.concat([df, df_them], ignore_index=True)
print(df)
df_nam = df[df["GioiTinh"] == "Nam"]
print(df_nam)
df_nu_hcm = df[(df["GioiTinh"] == "Nu") & (df["DiaChi"] == "HCM")]
print(df_nu_hcm)
print("Số sinh viên:", len(df_nu_hcm))
df_nu_hcm.to_csv("nu_hcm.csv", index=False, encoding="utf-8-sig")