import bpy
contextAreaType = bpy.context.area.type  # 現在のエリアタイプ
contextMode = bpy.context.mode  # 現在のモード

contextBone = bpy.context.active_pose_bone  # 現在のボーン
contextObject = bpy.context.object  # 現在のオブジェクト

bpy.context.area.type = 'VIEW_3D'  # ↓の理由で一度'3D Viewport'に切り替える
bpy.ops.view3d.snap_cursor_to_selected()  # '3D Viewport'じゃないとエラーになる

# 3Dカーソルの位置にポイントを足す
bpy.ops.object.mode_set(mode='OBJECT')  # ポイントを足すためにオブジェクトモードに切り替え
cursorLocation = bpy.context.scene.cursor.location  # カーソルの位置を取得
bpy.ops.object.empty_add(type='PLAIN_AXES', location=cursorLocation)  # ポイントを作成（カーソル位置適用）※選択が移る
bpy.context.object.name = (bpy.context.object.name + "(" + contextBone.name + ")")

# 状態を戻す
bpy.context.view_layer.objects.active = contextObject  # アーマチュアを選択（POSEモードに戻せない）
bpy.ops.object.mode_set(mode='POSE')

# ビューの設定を戻す
bpy.context.area.type = contextAreaType
