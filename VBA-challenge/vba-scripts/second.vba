Sub greatestvalues()
    Dim gitck As String
    Dim gi As Double
    Dim gdtck As String
    Dim gd As Double
    Dim gvtck As String
    Dim gv As Variant
    For i = 2 To 3001
        ' 2018:3001
        ' 2019:3001
        ' 2020:3001
        If IsEmpty(Cells(i + 1, 11).Value) Then
            Exit For
        End If
        If (i = 2) Then
            gi = Cells(i, 11).Value
            gitck = Cells(i, 9).Value
            gd = Cells(i, 11).Value
            gdtck = Cells(i, 9).Value
            gv = Cells(i, 12).Value
            gvtck = Cells(i, 9).Value
        End If
        If (gi >= Cells(i, 11).Value) Then
            ' do nothing
        Else
            gi = Cells(i, 11).Value
            gitck = Cells(i, 9).Value
        End If
        If (gd <= Cells(i, 11).Value) Then
            ' do nothing
        Else
            gd = Cells(i, 11).Value
            gdtck = Cells(i, 9).Value
        End If
        If (gv >= Cells(i, 12).Value) Then
            ' do nothing
        Else
            gv = Cells(i, 12).Value
            gvtck = Cells(i, 9).Value
        End If
    Next i
    Range("O2").Value = gitck
    Range("P2").Value = Format(gi, "0.00%")
    Range("O3").Value = gdtck
    Range("P3").Value = Format(gd, "0.00%")
    Range("O4").Value = gvtck
    Range("P4").Value = gv
End Sub