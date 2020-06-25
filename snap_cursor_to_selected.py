import bpy
contextAreaType = bpy.context.area.type
bpy.context.area.type = 'VIEW_3D'  # ↓の理由で一度'3D Viewport'に切り替える
bpy.ops.view3d.snap_cursor_to_selected()  # '3D Viewport'じゃないとエラーになる
bpy.context.area.type = contextAreaType  # ビューの設定を戻す
