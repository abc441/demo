function showSelection() {
            // 获取选中的性别值
            const selectedSex = document.querySelector('input[name="sex"]:checked').value;
            console.log(selectedSex);  //输出选中的性别值
            // 更新页面上的结果显示
            document.getElementById('result').innerText = `你选择的性别是：${selectedSex}`;
        }