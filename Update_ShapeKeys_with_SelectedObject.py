# --------------------------------------------------------------------------
# Update shape key with selected object
# --------------------------------------------------------------------------
# 選択したオブジェクトで対象のシェイプキーをミックス一括更新
# 1．ミックス対象のオブジェクトを選択
# 2．更新対象のオブジェクトをシフト選択
# 3．実行
#
# ※ ちゃんとした機能は全然実装してないので、今後の更新しだい？
# 200625 初期テスト版
# --------------------------------------------------------------------------

import bpy

AObj = bpy.context.active_object

# まずコピー
bpy.ops.object.join_shapes()

# 総数ゲット
ShapeKeyCo = len(AObj.data.shape_keys.key_blocks)
print("Shape Key Count = " + str(ShapeKeyCo))  # 確認print

# コピーしたターゲットを1番に移動
AObj.active_shape_key_index = (ShapeKeyCo)
bpy.ops.object.shape_key_move(type='TOP')

# No1のキーを1にする
AObj.active_shape_key_index = 1
AObj.active_shape_key.value = 1

# No2~のキーを1にして、名前をゲット
for i in range(2, ShapeKeyCo):
    AObj.active_shape_key_index = 2
    AObj.active_shape_key.value = 1
    NewName = AObj.active_shape_key.name  # 名前取得
    AObj.active_shape_key.name = NewName + "__old"  # 名前変更

    print("No = {0}, {1}".format(i, NewName))

    # 合成したシェイプキーを生成
    bpy.ops.object.shape_key_add(from_mix=True)
    AObj.active_shape_key.name = NewName

    # No2を消す
    AObj.active_shape_key_index = 2
    bpy.ops.object.shape_key_remove(all=False)

# Bisisを削除
AObj.active_shape_key_index = 0
bpy.ops.object.shape_key_remove(all=False)
AObj.active_shape_key.name = "Basis"
