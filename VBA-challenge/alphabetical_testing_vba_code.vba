Sub typvchanges()
    Dim tsv As Double
    Dim pc As Double
    Dim yc As Double
    Dim tck As String
    Dim opn As Double
    Dim cls As Double
    Dim cellnum As Double
    cellnum = 2
    For i = 2 To 30867
    ' A:22771
    ' B:25554
    ' C:26313
    ' D:30867
    ' E:22518
    ' F:30867
        tsv = 0
        tck = Cells(i, 1).Value
        opn = Cells(i, 3).Value
        While (tck = Cells(i + 1, 1))
            tsv = tsv + Cells(i, 7).Value
            i = i + 1
        Wend
        cls = Cells(i, 6).Value
        yc = cls - opn
        pc = (yc / opn) * 100
        tsv = tsv + Cells(i, 7).Value
        Cells(cellnum, 9).Value = tck
        Cells(cellnum, 10).Value = yc
        Cells(cellnum, 11).Value = pc
        Cells(cellnum, 12).Value = tsv
        If (yc < 0) Then
            Cells(cellnum, 10).Interior.ColorIndex = 3
        Else
            Cells(cellnum, 10).Interior.ColorIndex = 4
        End If
        cellnum = cellnum + 1
    Next i
End Sub

Sub greatestvalues()
    Dim gitck As String
    Dim gi As Double
    Dim gdtck As String
    Dim gd As Double
    Dim gvtck As String
    Dim gv As Variant
    For i = 2 To 123
        ' A:91
        ' B:102
        ' C:105
        ' D:123
        ' E:90
        ' F:123
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
    Range("P2").Value = gi
    Range("O3").Value = gdtck
    Range("P3").Value = gd
    Range("O4").Value = gvtck
    Range("P4").Value = gv
End Sub
